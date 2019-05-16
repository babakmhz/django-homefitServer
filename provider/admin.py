from django.contrib import admin
# Register your models here.
from provider.models import provider

# admin.site.register(personel_id)

# class provider_admin(admin.ModelAdmin):
# def get_readonly_fields(self,request,obj=None):
# return ['account_balance','address']
from django.contrib.auth.admin import UserAdmin
from provider.models import provider,services
from django.db import models
from django.forms import CheckboxSelectMultiple

# TODO:  make all models read-only
@admin.register(provider)
class ProvidingSkills(admin.ModelAdmin):
    list_display = ('name', 'phone', 'location', 'providing_category',)
    fields = ('name', 'phone', 'location',
              'providing_category', 'providing_services')
    filter_horizontal = ('providing_services',)


@admin.register(services)
class servicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'provider')

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
