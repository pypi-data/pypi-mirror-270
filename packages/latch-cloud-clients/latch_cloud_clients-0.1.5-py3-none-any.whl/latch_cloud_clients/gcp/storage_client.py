from collections.abc import AsyncGenerator
from typing import Any

from google.api_core.exceptions import (
    NotFound,
)

# from latch_o11y.o11y import trace_function_with_span
# from opentelemetry.trace import Span, get_tracer
from types_aiobotocore_s3.type_defs import (
    CompletedPartTypeDef,
)

from latch_cloud_clients.gcp.storage import Object

from ..utils import BlobMeta, EmptyMountResponseError, StorageClient
from .client_pool import gcp_pool


class GCPStorageClient(StorageClient):
    async def head(self, bucket_name: str, key: str) -> BlobMeta:
        # s.set_attributes({"bucket_name": bucket_name, "key": key})
        async with gcp_pool.gcp_client() as gcp:
            client = gcp.storage_client()
            blob = await client.get_blob_meta(bucket_name, key)

            if blob is None:
                blobs = []
                it = client.list_blobs(
                    bucket_name,
                    prefix=key.rstrip("/"),
                    delimiter="/",
                    max_items=1,
                    include_trailing_delimeter=True,
                    include_folders_as_prefixes=True,
                )
                async for blob in it:
                    blobs.append(blob)

                if len(blobs) > 0:
                    blob = blobs[0]
                else:
                    if len(it.prefixes) == 0:
                        raise EmptyMountResponseError()

                    if key.rstrip("/") not in [p.rstrip("/") for p in it.prefixes]:
                        raise EmptyMountResponseError()

                    blob = Object(
                        id=key,
                        bucket=bucket_name,
                        name=key,
                        content_type="dir",
                        media_link=None,
                        size=0,
                        generation=None,
                        update_time=None,
                        creation_time=None,
                    )

            blob = BlobMeta(
                bucket=bucket_name,
                key=key,
                content_type=blob.content_type,
                size=blob.size,
                version=blob.generation,
                update_time=blob.update_time,
            )

            return blob

    async def get_blob_bytes(
        self,
        bucket_name: str,
        key: str,
        start: int | None = None,
        end: int | None = None,
    ) -> bytes:
        # s.set_attributes({"bucket_name": bucket_name, "key": key})
        async with gcp_pool.gcp_client() as gcp:
            client = gcp.storage_client()

            try:
                return await client.get_blob_bytes(
                    bucket_name, key, start=start, end=end
                )
            except NotFound as e:
                raise EmptyMountResponseError() from e

    async def list_keys(
        self,
        bucket_name: str,
        prefix: str | None = None,
        delimiter: str = "/",
    ) -> AsyncGenerator[str, Any]:
        # s.set_attributes(
        #     {
        #         "bucket_name": bucket_name,
        #         "prefix": str(prefix),
        #         "delimeter": delimiter,
        #         "page_size": page_size,
        #     }
        # )
        async with gcp_pool.gcp_client() as gcp:
            client = gcp.storage_client()

            iterator = client.list_blobs(
                bucket_name,
                prefix=prefix,
                delimiter=delimiter,
            )

            async for obj in iterator:
                # don't add the prefix itself to the list
                if prefix is None or obj.name.rstrip("/") != prefix.rstrip("/"):
                    yield obj.name

            # all the prefixes are present after executing iterator above
            blob_prefixes = set(iterator.prefixes)

            for p in blob_prefixes:
                if prefix is None or p.rstrip("/") != prefix.rstrip("/"):
                    yield p

            return

    async def put_blob(
        self,
        bucket_name: str,
        key: str,
        body: bytes = b"",
        content_type: str | None = None,
        acl: str = "bucket-owner-full-control",
    ) -> BlobMeta:
        # s.set_attributes({"bucket_name": bucket_name, "key": key})

        async with gcp_pool.gcp_client() as gcp:
            client = gcp.storage_client()

            content_type = content_type if content_type else "text/plain"

            obj = await client.put_blob(
                bucket_name, key, body, content_type=content_type
            )

            return BlobMeta(
                bucket=bucket_name,
                key=key,
                content_type=content_type,
                size=len(body),
                version=obj.generation,
                update_time=obj.update_time,
            )

    async def copy_blob(
        self,
        src_key: str,
        src_bucket_name: str,
        dest_key: str,
        dest_bucket_name: str,
    ) -> None:
        # s.set_attributes(
        #     {
        #         "src_key": src_key,
        #         "src_bucket_name": src_bucket_name,
        #         "dest_key": dest_key,
        #         "dest_bucket_name": dest_bucket_name,
        #     }
        # )

        async with gcp_pool.gcp_client() as gcp:
            client = gcp.storage_client()

            try:
                await client.copy_blob(
                    src_bucket_name=src_bucket_name,
                    src_bucket_key=src_key,
                    dest_bucket_name=dest_bucket_name,
                    dest_bucket_key=dest_key,
                )
            except NotFound as e:
                # s.record_exception(e)
                raise EmptyMountResponseError from e

    async def copy_blob_multipart(
        self,
        src_key: str,
        src_bucket: str,
        dest_key: str,
        dest_bucket: str,
    ) -> None:
        # s.set_attributes(
        #     {
        #         "src_key": src_key,
        #         "src_bucket": src_bucket,
        #         "dest_key": dest_key,
        #         "dest_bucket": dest_bucket,
        #     }
        # )
        await self.copy_blob(src_key, src_bucket, dest_key, dest_bucket)

    async def delete_blob(
        self,
        bucket_name: str,
        key: str,
    ) -> None:
        # s.set_attributes({"bucket_name": bucket_name, "key": key})
        async with gcp_pool.gcp_client() as gcp:
            await gcp.storage_client().delete_blob(bucket_name, key)

    async def generate_signed_download_url(
        self,
        bucket_name: str,
        key: str | None,
        content_disposition: str | None = None,
        content_type: str | None = None,
    ) -> str:
        # s.set_attributes(
        #     {
        #         "bucket_name": bucket_name,
        #         "key": str(key),
        #         "content_disposition": str(content_disposition),
        #         "content_type": str(content_type),
        #     }
        # )
        async with gcp_pool.gcp_client() as gcp:
            url = gcp.storage_client().get_signed_download_url(
                bucket_name=bucket_name,
                key=key,
                content_disposition=content_disposition,
                content_type=content_type,
            )

            return url

    async def generate_signed_part_upload_url(
        self,
        bucket_name: str,
        bucket_key: str,
        upload_id: str,
        part_number: int,
    ) -> str:
        # s.set_attributes(
        #     {
        #         "bucket_name": bucket_name,
        #         "bucket_key": bucket_key,
        #         "idx": part_number,
        #     }
        # )

        async with gcp_pool.gcp_client() as gcp:
            return await gcp.storage_client().get_signed_part_upload_url(
                bucket_name=bucket_name,
                bucket_key=bucket_key,
                upload_id=upload_id,
                part_number=part_number,
            )

    async def multipart_initiate_upload(
        self,
        bucket_name: str,
        bucket_key: str,
        content_type: str,
        acl: str = "storageAdmin",
    ) -> str:
        # s.set_attributes(
        #     {
        #         "bucket_name": bucket_name,
        #         "key": bucket_key,
        #         "content_type": content_type,
        #         "acl": acl,
        #     }
        # )
        async with gcp_pool.gcp_client() as gcp:
            return await gcp.storage_client().multipart_initiate_upload(
                bucket_name, bucket_key, content_type
            )

    async def multipart_upload_part(
        self,
        bucket_name: str,
        bucket_key: str,
        upload_id: str,
        part_number: int,
        data: bytes,
    ) -> str:
        async with gcp_pool.gcp_client() as gcp:
            return await gcp.storage_client().multipart_upload_part(
                bucket_name, bucket_key, upload_id, part_number, data
            )

    async def multipart_complete_upload(
        self,
        bucket_name: str,
        bucket_key: str,
        upload_id: str,
        parts: list[CompletedPartTypeDef],
    ) -> str:
        # s.set_attributes(
        #     {
        #         "bucket_name": bucket_name,
        #         "bucket_key": bucket_key,
        #     }
        # )
        async with gcp_pool.gcp_client() as gcp:
            return await gcp.storage_client().multipart_complete_upload(
                bucket_name, bucket_key, upload_id, parts
            )
