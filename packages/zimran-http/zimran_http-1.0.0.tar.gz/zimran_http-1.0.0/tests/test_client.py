from zimran.http_client import AsyncHttpClient as HttpClient


async def test_client(httpx_mock):
    httpx_mock.add_response(url='http://example.com/', json={'hello': 'world'})

    client = HttpClient(base_url='http://example.com')

    response = await client.get('/')

    assert response.status_code == 200


async def test_client_custom_handler(httpx_mock):
    httpx_mock.add_response(url='http://example.com/', json={'hello': 'world'})

    client = HttpClient(base_url='http://example.com')

    async def custom_handler(response):
        assert response.status_code == 200
        assert response.json() == {'hello': 'world'}

    response = await client.get('/', response_handler=custom_handler)

    assert response is None  # Since custom_handler doesn't return anything
