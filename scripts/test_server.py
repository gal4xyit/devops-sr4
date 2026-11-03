from aiohttp import web
from sr4_demo import hello


async def health(request):
    return web.json_response({
        "status": "ok",
        "message": hello(),
    })


app = web.Application()
app.router.add_get("/health", health)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080, access_log=None)
