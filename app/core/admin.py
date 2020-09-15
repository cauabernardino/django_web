from django.contrib import admin

from .models import Person, TimesISaved, TimesYouSaved

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('modified', 'name')


@admin.register(TimesISaved)
class TimesISavedAdmin(admin.ModelAdmin):
    list_display = ('modified', 'when', 'how', 'get_thanks')


@admin.register(TimesYouSaved)
class TimesYouSavedAdmin(admin.ModelAdmin):
    list_display = ('modified', 'when', 'how', 'get_thanks')
