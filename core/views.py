from django.views.generic import TemplateView
from core import models

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['depoimentos'] = models.Depoimentos.objects.all()
        context['redes_sociais']=models.Redes_Sociais.objects.all()
        context['downloads'] = models.Downloads.objects.all()
        return context

class ArticleView(TemplateView):
    template_name = 'article.html'
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['redes_sociais']=models.Redes_Sociais.objects.all()
        return context

class PrivacyView(TemplateView):
    template_name = 'privacy.html'
    def get_context_data(self, **kwargs):
        context = super(PrivacyView, self).get_context_data(**kwargs)
        context['redes_sociais']=models.Redes_Sociais.objects.all()
        return context

class TermsView(TemplateView):
    template_name = 'terms.html'
    def get_context_data(self, **kwargs):
        context = super(TermsView, self).get_context_data(**kwargs)
        context['redes_sociais']=models.Redes_Sociais.objects.all()
        return context