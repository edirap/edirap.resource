from collective.grok import gs
from edirap.resource import MessageFactory as _

@gs.importstep(
    name=u'edirap.resource', 
    title=_('edirap.resource import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('edirap.resource.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
