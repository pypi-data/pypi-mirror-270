from typing import Any, Callable

import httpx

try:
    from loguru import logger

except ImportError:
    import logging

    logger = logging.getLogger(__name__)


class HttpClient:
    DEFAULT_TIMEOUT = 10

    def __init__(self, *, base_url: str) -> None:
        self.session = httpx.AsyncClient(base_url=base_url)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.close()

    async def close(self):
        if not self.session.is_closed:
            await self.session.aclose()

    async def _perform_request(self, *, method: str, url: str, **kwargs: dict[str, Any]):
        kwargs.setdefault('timeout', self.DEFAULT_TIMEOUT)

        logger.info(f'Performing {method.upper()} request to {url}')

        return await self.session.request(method=method, url=url, **kwargs)

    async def get(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = await self._perform_request(method='get', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return await handler(response)

    async def post(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = await self._perform_request(method='post', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return await handler(response)

    async def patch(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = await self._perform_request(method='patch', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return await handler(response)

    async def put(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = await self._perform_request(method='put', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return await handler(response)

    async def delete(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = await self._perform_request(method='delete', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return await handler(response)

    async def options(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = await self._perform_request(method='options', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return await handler(response)

    async def handle_response(self, response: 'httpx.Response'):
        """Base implementation of httpx response handler"""

        return response
