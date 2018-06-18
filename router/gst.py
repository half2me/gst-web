from view.gst import *


def setup(app):
    pre = '/api/gst'
    app.router.add_get(pre + '/debug', getDebug)
    app.router.add_post(pre + '/debug', setDebug)
    app.router.add_get(pre + '/tracer', getTracer)
    app.router.add_post(pre + '/tracer', setTracer)
    app.router.add_get(pre + '/debug-file', getDebugFile)
    app.router.add_post(pre + '/debug-file', setDebugFile)
    app.router.add_get(pre + '/dot-dir', getDotDir)
    app.router.add_post(pre + '/dot-dir', setDotDir)
    app.router.add_post(pre + '/dot-snapshot', makeDotSnapshot)
    app.router.add_get(pre + '/elements', getAvailableElements)