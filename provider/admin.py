from django.contrib import admin
from provider.models import skill,skillTag
# Register your models here.
from provider.models import provider

admin.site.register(skill)
admin.site.register(skillTag)
#admin.site.register(personel_id)

class provider_admin(admin.ModelAdmin):
    def get_readonly_fields(self,request,obj=None):
        return ['account_balance','address']
admin.site.register(provider,provider_admin)

## TODO:  make all models read-only
