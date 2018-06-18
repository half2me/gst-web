from router import *
from views import *


def setup_routes(app):
    app.router.add_get('/', index)

    gst.setup(app)
    pipeline.setup(app)

    app.router.add_get('/ws', ws_handler)

    # Fallback static route
    app.router.add_static('/', path='api/static', name='static')
