from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Person, TimesISaved, TimesYouSaved
from .forms import TimesYouSavedModelForm



class IndexView(TemplateView):
    """
    View for Times I Save page
    """
    template_name = 'index.html'

    # Getting data from db
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        context['times'] = TimesISaved.objects.all()

        return context


class YouSaveView(TemplateView):
    """
    View for Times You Saved page
    """
    template_name = 'yousave.html'
    form_class = TimesYouSavedModelForm
    success_url = reverse_lazy('yousave')

    # Getting data from db
    def get_context_data(self, **kwargs):
        context = super(YouSaveView, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        context['times'] = TimesYouSaved.objects.all()

        return context



class ContactView(TemplateView):
    """
    View for Contact page
    """
    template_name = 'contact.html'