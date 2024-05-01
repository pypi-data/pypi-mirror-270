## Installation

```bash
pip install zimran-http
```

## Usage

```python
from zimran.http_client import AsyncHttpClient, HttpClient

# async
async with AsyncHttpClient(service='...') as client:
    response = await client.get('/endpoint')

# sync
client = HttpClient(service='...')
response = client.get('/endpoint')


# custom response handler
async def custom_handler(response: httpx.Response):
  # your logic with response handler here
  ...


response = await client.get('/endpoint', response_handler=custom_handler)

```
