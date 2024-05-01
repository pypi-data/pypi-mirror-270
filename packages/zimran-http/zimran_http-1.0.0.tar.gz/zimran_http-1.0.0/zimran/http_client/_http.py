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
        self.session = httpx.Client(base_url=base_url)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def close(self):
        if not self.session.is_closed:
            self.session.close()

    def _perform_request(self, *, method: str, url: str, **kwargs: dict[str, Any]):
        kwargs.setdefault('timeout', self.DEFAULT_TIMEOUT)

        logger.info(f'Performing {method.upper()} request to {url}')

        return self.session.request(method=method, url=url, **kwargs)

    def get(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = self._perform_request(method='get', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return handler(response)

    def post(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = self._perform_request(method='post', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return handler(response)

    def patch(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = self._perform_request(method='patch', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return handler(response)

    def put(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = self._perform_request(method='put', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return handler(response)

    def delete(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = self._perform_request(method='delete', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return handler(response)

    def options(self, url: str, *, response_handler: Callable | None = None, **kwargs):
        response = self._perform_request(method='options', url=url, **kwargs)

        handler = response_handler or self.handle_response

        return handler(response)

    def handle_response(self, response: 'httpx.Response'):
        """Base implementation of httpx response handler"""

        return response
