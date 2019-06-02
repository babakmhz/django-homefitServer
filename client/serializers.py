from rest_framework import serializers
from client.models import (bannerSlider,
                           user,
                           serviceCategory,
                           subServiceCategory,
                           availableDateTimeService,
                           serviceDate,
                           serviceTime,
                           order)

from client import Utils
import decimal

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


class submitOrderSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        # TODO: remove client from here and get client by token
        model = order
        fields = ('id', 'services', 'dateTime',
                  'orderNumber',
                  'location',
                  'client',
                  'provider',
                  'status',
                  'total_cost')
        read_only_fields = ('id', 'orderNumber', 'client', 'status')
        #extra_kwargs = {'orderTags': {'write_only': True}}

    def create(self, validated_data):
        request = self.context['request']
        this_client = user.objects.filter(
            token__token=request.META.get('HTTP_AUTHORIZATION')).get()

        # this_provider = user.objects.filter(
            # id=validated_data.get('provider')).get()
            
        this_provider = validated_data.get('provider')

        orders = order(services=self.get_services(None), provider=this_provider, orderNumber='{}'.format(Utils.appUtils.generateOrderNumber()),
                       client=this_client,
                       location=validated_data.get('location'), status='{}'.format('IP'),
                       total_cost=validated_data.get('total_cost'),
                       dateTime=validated_data.get('dateTime'))
        orders.save()

        return orders

    def get_status(self, order):
        return 'IP'

    def get_services(self, order):
        request = self.context['request']
        services = Utils.appUtils.resolveArrayToList(request.POST.get('services'))
        f = ''
        for service in services:
            f = f + str(subServiceCategory.objects.filter(id=service).get())+','
        return f
