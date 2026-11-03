from molotov import scenario


@scenario(weight=100, delay=0.1)
async def checkJson(session):
    async with session.get("http://127.0.0.1:8080/health") as response:
        assert response.status == 200, response.status

        data = await response.json()
        assert data == {
            "status": "ok",
            "message": "Hello from SR4!",
        }, data
