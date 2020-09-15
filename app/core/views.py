from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.shortcuts import render

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


class YouSaveView(FormView):
    """
    View for Times You Saved page
    """
    template_name = 'yousave.html'
    form_class = TimesYouSavedModelForm

    # Getting data from db
    def get_context_data(self, **kwargs):
        context = super(YouSaveView, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        context['times'] = TimesYouSaved.objects.all()

        return context
    
    def post(self, request):
        
        form = self.form_class(request.POST or None)

        if form.is_valid():
            
            form.save()

            return HttpResponseRedirect(self.request.path_info)

        return render(request, self.template_name, {'form': form})


class ContactView(TemplateView):
    """
    View for Contact page
    """
    template_name = 'contact.html'