from django.contrib import admin
from .models import djangoClasses


# Register your models here.
class DjangoAdmin(admin.ModelAdmin):
    pass


admin.site.register(djangoClasses, DjangoAdmin)
