from django.contrib import admin

# Register your models here.

from .models import Blogpost,contact

admin.site.register(Blogpost)


admin.site.register(contact)

# admin.site.register(UserImformation)