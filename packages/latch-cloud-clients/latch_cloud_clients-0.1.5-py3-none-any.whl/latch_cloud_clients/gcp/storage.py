from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any, TypedDict
from urllib.parse import quote, urljoin
from xml.etree import ElementTree as ET

import aiohttp
import xmltodict
from google.api_core.exceptions import (
    BadRequest,
    Forbidden,
    NotFound,
    ServerError,
    TooManyRequests,
    Unauthorized,
)
from google.auth import default
from google.auth.transport import requests
from google.cloud import storage

max_presigned_url_age = timedelta(days=7) // timedelta(seconds=1)


@dataclass(frozen=True)
class Bucket:
    name: str
    id: str
    creation_time: str
    update_time: str
    project_number: str


@dataclass(kw_only=True)
class Object:
    id: str
    name: str
    bucket: str
    size: int
    media_link: str | None
    generation: str | None
    content_type: str | None
    creation_time: datetime | None
    update_time: datetime | None


CompletedPartTypeDef = TypedDict(
    "CompletedPartTypeDef",
    {
        "ETag": str,
        "ChecksumCRC32": str,
        "ChecksumCRC32C": str,
        "ChecksumSHA1": str,
        "ChecksumSHA256": str,
        "PartNumber": int,
    },
    total=False,
)


class AsyncStorageClient:
    credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])

    def __init__(self, session: aiohttp.ClientSession):
        self.api_url = "https://storage.googleapis.com/storage/v1/"
        self.upload_api_url = "https://storage.googleapis.com/upload/storage/v1/"
        self.session = session

    @staticmethod
    def get_auth_token():
        credentials = AsyncStorageClient.credentials

        if credentials.token is None or credentials.expired:
            credentials.refresh(requests.Request())
        return credentials.token

    async def _make_api_request(
        self,
        method: str,
        url: str,
        *,
        data: Any | None = None,
        headers: dict | None = None,
        params: dict | None = None,
        return_bytes=False,
        return_json=False,
        return_response=False,
    ) -> Any:
        if headers is None:
            headers = {}

        headers["Authorization"] = f"Bearer {AsyncStorageClient.get_auth_token()}"

        async with self.session.request(
            method,
            url,
            headers=headers,
            params=params,
            data=data,
        ) as resp:
            if resp.status >= 400:
                err = await resp.text()
                if resp.status == 400:
                    raise BadRequest(message=err, response=resp)
                if resp.status == 401:
                    raise Unauthorized(message=err, response=resp)
                if resp.status == 403:
                    raise Forbidden(message=err, response=resp)
                if resp.status == 404:
                    raise NotFound(message=err, response=resp)
                if resp.status == 429:
                    raise TooManyRequests(message=err, response=resp)
                raise ServerError(message=err, response=resp)
            if resp.status == 204:
                return
            if return_bytes:
                return await resp.content.read()
            if return_json:
                return await resp.json()
            if return_response:
                return resp
            return await resp.text()

    async def get_bucket(self, bucket_name: str):
        try:
            res = await self._make_api_request(
                "GET",
                urljoin(
                    self.api_url,
                    f"b/{bucket_name}",
                ),
                return_json=True,
            )
        except NotFound:
            return None

        return Bucket(
            name=res["name"],
            id=res["id"],
            creation_time=res["timeCreated"],
            update_time=res["updated"],
            project_number=res["projectNumber"],
        )

    async def get_blob_meta(self, bucket_name: str, key: str):
        try:
            res = await self._make_api_request(
                "GET",
                urljoin(self.api_url, f"b/{bucket_name}/o/{quote(key, safe='')}"),
                return_json=True,
            )
        except NotFound:
            return None

        return Object(
            name=res["name"],
            id=res["id"],
            bucket=res["bucket"],
            media_link=res["mediaLink"],
            generation=res["generation"],
            content_type=res["contentType"],
            size=int(res["size"]),
            creation_time=datetime.fromisoformat(res["timeCreated"]),
            update_time=datetime.fromisoformat(res["updated"]),
        )

    def list_blobs(
        self,
        bucket_name: str,
        prefix: str | None = None,
        delimiter: str = "/",
        match_glob: str | None = None,
        page_token: str | None = None,
        include_trailing_delimeter: bool | None = None,
        include_folders_as_prefixes: bool | None = None,
        max_items: int | None = None,
    ):
        if match_glob is not None and delimiter != "/":
            raise ValueError("match_glob is only supported with delimeter='/'")

        if include_folders_as_prefixes and delimiter != "/":
            raise ValueError(
                "include_folders_as_prefixes is only supported with delimeter='/'"
            )

        params = {
            "bucket": bucket_name,
            "prefix": prefix,
            "delimiter": delimiter,
            "matchGlob": match_glob,
            "maxResults": 1000,
            "pageToken": page_token,
            "includeTrailingDelimeter": include_trailing_delimeter,
            "includeFoldersAsPrefixes": include_folders_as_prefixes,
        }

        params = {k: str(v) for k, v in params.items() if v is not None}

        return AsyncHTTPIterator(
            url=urljoin(self.api_url, f"b/{bucket_name}/o"),
            headers={},
            params=params,
            storage_client=self,
            max_items=max_items,
        )

    async def get_blob_bytes(
        self,
        bucket_name: str,
        key: str,
        start: int | None = None,
        end: int | None = None,
    ):
        headers = {}
        if start is None:
            start = 0

        if end is not None:
            headers["Range"] = f"bytes={start}-{end}"

        return bytes(
            await self._make_api_request(
                "GET",
                urljoin(self.api_url, f"b/{bucket_name}/o/{quote(key, safe='')}"),
                params={"alt": "media"},
                headers=headers,
                return_bytes=True,
            )
        )

    async def put_blob(
        self,
        bucket_name: str,
        key: str,
        data: bytes,
        content_type: str | None = None,
    ):
        if content_type is None:
            content_type = "text/plain"

        resp = await self._make_api_request(
            "POST",
            urljoin(self.upload_api_url, f"b/{bucket_name}/o"),
            params={"name": key, "uploadType": "media"},
            headers={"Content-Type": content_type},
            data=data,
            return_json=True,
        )

        return Object(
            id=resp["id"],
            name=resp["name"],
            bucket=resp["bucket"],
            media_link=resp["mediaLink"],
            generation=resp["generation"],
            content_type=resp["contentType"],
            size=int(resp["size"]),
            creation_time=datetime.fromisoformat(resp["timeCreated"]),
            update_time=datetime.fromisoformat(resp["updated"]),
        )

    async def copy_blob(
        self,
        src_bucket_name: str,
        src_bucket_key: str,
        dest_bucket_name: str,
        dest_bucket_key: str,
    ):
        done = False
        rewrite_token = None
        try:
            while not done:
                params = {}
                if rewrite_token:
                    params = {"rewriteToken": rewrite_token}

                resp = await self._make_api_request(
                    "POST",
                    urljoin(
                        self.api_url,
                        f"b/{src_bucket_name}/o/{quote(src_bucket_key,safe='')}/rewriteTo/b/{dest_bucket_name}/o/{quote(dest_bucket_key, safe='')}",
                    ),
                    params=params,
                    headers={"Content-Type": "application/json"},
                    return_json=True,
                )

                done = resp["done"]
                rewrite_token = resp.get("rewriteToken", None)
        except NotFound:
            return None

    async def delete_blob(
        self, bucket_name: str, key: str, generation: str | None = None
    ):
        params = {}
        if generation is not None:
            params["generation"] = generation

        await self._make_api_request(
            "DELETE",
            urljoin(self.api_url, f"b/{bucket_name}/o/{quote(key, safe='')}"),
            params=params,
        )

    def get_signed_download_url(
        self,
        bucket_name: str,
        key: str | None,
        content_disposition: str | None = None,
        content_type: str | None = None,
    ):
        # note(taras): this constructs a blob object and signs download url without making requests
        blob = storage.Client().bucket(bucket_name).blob(key)

        return blob.generate_signed_url(
            version="v4",
            expiration=max_presigned_url_age,
            method="GET",
            content_type=content_type,
            response_disposition=content_disposition,
        )

    async def get_signed_part_upload_url(
        self,
        bucket_name: str,
        bucket_key: str,
        upload_id: str,
        part_number: int,
    ):

        # note(taras): this constructs a blob object and signs
        # upload url without making syncronous requests
        blob = storage.Client().bucket(bucket_name).blob(bucket_key)

        return blob.generate_signed_url(
            version="v4",
            expiration=max_presigned_url_age,
            method="PUT",
            query_parameters={
                "partNumber": part_number,
                "uploadId": upload_id,
            },
        )

    async def multipart_initiate_upload(
        self,
        bucket_name: str,
        bucket_key: str,
        content_type: str = "text/plain",
    ):
        meta = await self.get_blob_meta(bucket_name, bucket_key)
        if meta is None:
            await self.put_blob(bucket_name, bucket_key, b"")

        # note(taras): multipart uploads use XML api instead of JSON
        resp = await self._make_api_request(
            "POST",
            f"https://storage.googleapis.com/{bucket_name}/{bucket_key}?uploads",
            headers={
                "Content-Type": content_type,
            },
        )

        return str(xmltodict.parse(resp)["InitiateMultipartUploadResult"]["UploadId"])

    async def multipart_upload_part(
        self,
        bucket_name: str,
        bucket_key: str,
        upload_id: str,
        part_number: int,
        data: bytes,
    ) -> str:
        resp = await self._make_api_request(
            "PUT",
            f"https://storage.googleapis.com/{bucket_name}/{bucket_key}?uploadId={upload_id}&partNumber={part_number}",
            data=data,
            return_response=True,
        )

        return resp.headers["ETag"]

    async def multipart_complete_upload(
        self,
        bucket_name: str,
        bucket_key: str,
        upload_id: str,
        parts: list[CompletedPartTypeDef],
    ) -> str:
        root = ET.Element("CompleteMultipartUpload")

        for part in parts:
            if "PartNumber" not in part:
                raise ValueError("PartNumber is required")
            if "ETag" not in part:
                raise ValueError("ETag is required")

            part_element = ET.SubElement(root, "Part")
            ET.SubElement(part_element, "PartNumber").text = str(part["PartNumber"])
            ET.SubElement(part_element, "ETag").text = part["ETag"]

        await self._make_api_request(
            "POST",
            f"https://storage.googleapis.com/{bucket_name}/{bucket_key}?uploadId={upload_id}",
            data=ET.tostring(root),
        )

        blob = await self.get_blob_meta(bucket_name, bucket_key)
        if blob is None:
            raise ServerError("Failed to complete multipart upload: can't find blob")
        if blob.generation is None:
            raise ServerError("The uploaded blob has no generation")

        return blob.generation


class AsyncHTTPIterator:
    def __init__(
        self,
        url: str,
        headers: dict,
        params: dict,
        storage_client: AsyncStorageClient,
        max_items: int | None = None,
    ):
        self.url = url
        self.headers = headers
        self.params = params
        self.next_page_token = None
        self.prefixes: set[str] = set()
        self.items = []
        self.storage_client = storage_client

        self.cur_item = 0
        self.max_items = max_items

    def __aiter__(self):
        return self

    async def __anext__(self):
        if (self.max_items is not None and self.cur_item >= self.max_items) or (
            len(self.items) == 0 and self.next_page_token == ""
        ):
            raise StopAsyncIteration

        if len(self.items) > 0:
            obj = self.items.pop()
            self.cur_item = self.cur_item + 1

            creation_time = obj.get("timeCreated")
            if creation_time is not None:
                creation_time = datetime.fromisoformat(creation_time)

            update_time = obj.get("updated")
            if update_time is not None:
                update_time = datetime.fromisoformat(update_time)

            return Object(
                id=obj["id"],
                name=obj["name"],
                bucket=obj["bucket"],
                media_link=obj.get("mediaLink"),
                generation=obj.get("generation"),
                content_type=obj["contentType"],
                size=int(obj["size"]),
                creation_time=creation_time,
                update_time=update_time,
            )

        if self.next_page_token:
            self.params["pageToken"] = self.next_page_token

        res = await self.storage_client._make_api_request(
            "GET", self.url, headers=self.headers, params=self.params, return_json=True
        )

        self.items = res.get("items", [])
        prefixes = res.get("prefixes", [])
        self.next_page_token = res.get("nextPageToken", "")

        for prefix in prefixes:
            self.prefixes.add(prefix)

        if "items" not in res:
            raise StopAsyncIteration

        return await self.__anext__()
