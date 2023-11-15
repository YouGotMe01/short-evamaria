# Credit - adarsh-goel

from aiohttp import web
#from web.stream_routes import routes
routes = web.RouteTableDef()

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
