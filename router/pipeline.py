from api.view.pipeline import *


def setup(app):

    pre = '/api/pipelines'

    app.router.add_get(pre, get_pipes)
    app.router.add_put(pre, create_pipe)

    app.router.add_get(pre + '/{id}', getPipelineInfo)
    app.router.add_delete(pre + '/{id}', deletePipe)
    app.router.add_post(pre + '/{id}/start', startStream)
    app.router.add_post(pre + '/{id}/pause', pauseStream)
    app.router.add_post(pre + '/{id}/stop', stopStream)
    app.router.add_post(pre + '/{id}/reset', resetStream)

    app.router.add_put(pre + '/{pipeId}/elements', addElement)
    app.router.add_get(pre + '/{pipeId}/elements/{elementId}', getElementInfo)
    app.router.add_post(pre + '/{pipeId}/elements/{elementId}', setElementInfo)
    app.router.add_delete(pre + '/{pipeId}/elements/{elementId}', deleteElement)

    app.router.add_get(pre + '/{pipeId}/links', getLinks)
    app.router.add_put(pre + '/{pipeId}/links', newLink)
    app.router.add_delete(pre + '/{pipeId}/links', deleteLink)

