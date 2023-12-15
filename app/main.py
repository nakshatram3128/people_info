from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, this is your aiohttp endpoint!")

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    print("I am In")
    web.run_app(app, port=8998)
