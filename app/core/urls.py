from django.urls import path
from .views import IndexView, YouSaveView, ContactView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('yousave/', YouSaveView.as_view(), name='yousave'),
    path('contact/', ContactView.as_view(), name='contact') 
]