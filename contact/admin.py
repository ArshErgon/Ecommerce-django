from django.contrib import admin

from .models import ContactModel, AboutModel

admin.site.register(AboutModel)
admin.site.register(ContactModel)