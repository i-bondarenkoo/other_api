import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from main import app


# @pytest.fixture(scope="module") — фикстура создаёт одного клиента на все тесты в файле.
@pytest_asyncio.fixture(scope="module")
async def async_client():
    # AsyncClient(transport=ASGITransport(app=app), base_url="http://test") — создаёт асинхронного клиента для тестирования
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as client:
        yield client
