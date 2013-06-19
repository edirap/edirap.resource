from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class Type(grok.GlobalUtility):
    grok.name('edirap.resource.type')
    grok.implements(IVocabularyFactory)

    _terms = [
        {
            'value': 'policy',
            'title': u'Policy, Strategy, Plan',
        },
        { 
            'value': 'legislation',
            'title': u'Legislation, Regulation',
        },
        {
            'value': 'training',
            'title': u'Training, Guide'
        },
        {
             'value': 'project',
             'title': u'Project',
         },
        {
            'value': 'data',
            'title': u'Data, Survey'
            },
        {   'value': 'application',
            'title': 'Application, Product, Portal'},
    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(*i))
        return SimpleVocabulary(terms)
