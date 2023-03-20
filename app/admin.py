from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import User, Category

admin.site.register(User)
admin.site.register(Category, MPTTModelAdmin)
