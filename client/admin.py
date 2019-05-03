
from django.contrib import admin
from client.models import (orderTag,
                           serviceCategory,
                           serviceList, service,
                           bannerSlider,
                           subServiceCategory,
                           user,
                           token,
                           order,
                           service_tip,
                           warninig,
                           service_tip_text,
                           warninig_text,
                           ordered_service,
                           serviceDate,
                           serviceTime,
                           availableDateTimeService)

# Register your models here.
from django.contrib import admin
# you need import this for adding jalali calander widget
admin.site.register(bannerSlider)
admin.site.register(serviceCategory)
admin.site.register(subServiceCategory)
admin.site.register(user)
admin.site.register(token)
admin.site.register(orderTag)
admin.site.register(service)
admin.site.register(serviceList)
admin.site.register(service_tip)
admin.site.register(warninig)
admin.site.register(service_tip_text)
admin.site.register(warninig_text)
admin.site.register(serviceDate)
admin.site.register(serviceTime)
admin.site.register(availableDateTimeService)

# TODO: remove orderd_service from admin mode
admin.site.register(ordered_service)
# TODO:  make all models read-only
