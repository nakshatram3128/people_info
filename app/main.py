from aiohttp import web

async def sample(request):
    return web.Response(text="Hello, this is your aiohttp sample endpoint!")

async def handle(request):
    return web.Response(text="Hello, this is your aiohttp endpoint!")

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/sample', sample)


if __name__ == '__main__':
    web.run_app(app, port=8998)
