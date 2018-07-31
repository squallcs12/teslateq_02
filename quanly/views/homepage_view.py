from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from quanly.forms import LoginForm


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context.update({
            'form': LoginForm(),
        })
        return context

    def post(self, request):
        return TemplateResponse(request, self.template_name, {
            'form_da_submit': True,
        })
