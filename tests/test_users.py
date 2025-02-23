import pytest


@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.request(
        "POST",
        "/users/",
        json={"first_name": "John", "last_name": "Smith", "email": "john@example.com"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Smith"
    assert data["email"] == "john@example.com"


@pytest.mark.asyncio
async def test_get_user_by_id(async_client):
    response = await async_client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_get_all_users(async_client):
    response = await async_client.get("/users/?start=1&stop=3")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


@pytest.mark.asyncio
async def test_update_user_partial(async_client):
    responce = await async_client.request(
        "PATCH",
        "/users/2",
        json={"first_name": "Игорь", "email": "igor_igor@gmail.com"},
    )
    assert responce.status_code == 200
    data = responce.json()
    assert data["first_name"] == "Игорь"
    assert data["email"] == "igor_igor@gmail.com"
    assert data["id"] == 2


@pytest.mark.asyncio
async def test_update_user_full(async_client):
    responce = await async_client.request(
        "PUT",
        "/users/4",
        json={"first_name": "Иван", "last_name": "Иванов", "email": "123@gmail.com"},
    )
    assert responce.status_code == 200
    data = responce.json()
    assert data["first_name"] == "Иван"
    assert data["email"] == "123@gmail.com"
    assert data["id"] == 4


@pytest.mark.asyncio
async def test_delete_user(async_client):
    responce = await async_client.request(
        "DELETE",
        "/users/5",
    )
    assert responce.status_code == 200
    data = responce.json()
    assert data["detail"] == "Пользователь удален"
