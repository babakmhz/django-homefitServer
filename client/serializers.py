from rest_framework import serializers
from client.utils import OrderNumber
from client.models import (bannerSlider,
                           user,
                           serviceCategory,
                           subServiceCategory,
                           availableDateTimeService,
                           serviceDate,
                           serviceTime)

from provider.models import provider, availableDates


class bannerSliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = bannerSlider
        fields = '__all__'


class subServiceCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = subServiceCategory
        fields = '__all__'


class serviceCategoriesSerializer(serializers.ModelSerializer):
    service = subServiceCategoriesSerializer(many=True)

    class Meta:

        model = serviceCategory
        fields = ('id',
                  'title',
                  'title_arabic',
                  'image',
                  'image_selected',
                  'service')



# class submitOrderSerializer(serializers.ModelSerializer):
#     #orderTags = serializers.ListField(child=orderTagsSerializer())
#     #orderTags = serializers.SerializerMethodField('get_tags')
#     service = serializers.SerializerMethodField('get_services')

#     class Meta:
#         # TODO: remove client from here and get client by token
#         model = order
#         fields = ('id',
#                   'service',
#                   'client',
#                   'orderNumber',
#                   'gender',
#                   'dateTime',
#                   'location_coordinates_or_address',)
#         read_only_fields = ('id', 'orderNumber', 'client', 'dateTime',)
#         #extra_kwargs = {'orderTags': {'write_only': True}}

#     def create(self, validated_data):
#         request = self.context['request']
#         this_client = user.objects.filter(
#             token__token=request.META.get('HTTP_AUTH')).get()
#         orders = order(service='{}'.format(self.get_services(order=None)), orderNumber='{}'.format(OrderNumber.generate()),
#                        client=this_client, location_coordinates_or_address=validated_data.get('location_coordinates_or_address'))
#         orders.save()
#         services = request.data.get('service')
#         for service in services:
#             ordered_service.objects.create(
#                 service=serviceList.objects.filter(id=service).get(), _order=orders)

#         return orders

#     def get_gender(self, order):
#         if not order.gender:
#             return 'M'

#     def get_services(self, order):
#         services = self.context['request'].data.get('service')
#         names = ''
#         for service in services:
#             this_service = str(serviceList.objects.filter(id=service).get())
#             names = names+' , ' + this_service
#         return names
