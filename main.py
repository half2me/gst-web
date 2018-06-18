#!/usr/bin/env python3

import gbulb
from aiohttp import web

from router import setup_routes
from view import setup_view

gbulb.install()  # Use Glib Mainloop implementation

app = web.Application()
setup_routes(app)
setup_view(app)

app['logic'] = Logic()
app['ws'] = {}
app.on_startup.append(app['logic'].onStartup)
app.on_shutdown.append(app['logic'].onShutdown)

web.run_app(app, host='0.0.0.0', port=80)