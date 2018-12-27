from rest_framework import serializers
from client.utils import OrderNumber
from provider.models import skillTag
from client.models import (bannerSlider,
                user,
                serviceCategory,
                order,
                subServiceCategory,
                orderTag,
                service,
                serviceList,
                service_tip,
                service_tip_text,
                ordered_service,)

class bannerSliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = bannerSlider
        fields = '__all__'

class subServiceCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = subServiceCategory
        fields = '__all__'


class profilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('profile_photo',)
        ## TODO: remove privious uploaded pics

class IdCardPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id_card_photo',)
        ## TODO: remove privious uploaded pics

class serviceCategoriesSerializer(serializers.ModelSerializer):
    category = subServiceCategoriesSerializer(many=True)
    class Meta:
        model = serviceCategory
        fields = ('id','title','image','category',)

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('first_name','last_name','id_number','id_card_photo')

class getUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','phone_number',
                     'first_name',
                     'last_name',
                     'gender',
                     'profile_status',
                     'push_id',
                     'account_balance',
                     'profile_photo',
                     'id_number')

class updateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('first_name',
                    'last_name',
                    'gender',
                    'id_number',)

class orderTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderTag
        fields = '__all__'

class serviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = serviceList
        fields = '__all__'


class servicesSerializer(serializers.ModelSerializer):
    services = serviceListSerializer(many=True)
    class Meta:
        model = service
        fields = ('id','title_preview','title','minimum_cost','image','category','description','services')

class tipSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_tip_text
        fields = '__all__'

class serviceTipSerializer(serializers.ModelSerializer):
    tip = tipSerializer(many=False)
    class Meta:
        model = service_tip
        fields = ('id','tip')

class submitOrderSerializer(serializers.ModelSerializer):
    #orderTags = serializers.ListField(child=orderTagsSerializer())
    #orderTags = serializers.SerializerMethodField('get_tags')
    service = serializers.SerializerMethodField('get_services')
    class Meta:
        # TODO: remove client from here and get client by token
        model = order
        fields = ('id',
                        'service',
                        'client',
                        'orderNumber',
                        'gender',
                        'dateTime',
                        'location_coordinates_or_address',)
        read_only_fields = ('id','orderNumber','client','dateTime',)
        #extra_kwargs = {'orderTags': {'write_only': True}}
    def create(self,validated_data):
        request = self.context['request']
        this_client = user.objects.filter(token__token=request.META.get('HTTP_AUTH')).get()
        orders = order(service = '{}'.format(self.get_services(order=None)),orderNumber='{}'.format(OrderNumber.generate()),
        client = this_client,location_coordinates_or_address=validated_data.get('location_coordinates_or_address'))
        orders.save()
        services = request.data.get('service')
        for service in services:
            ordered_service.objects.create(service=serviceList.objects.filter(id=service).get(),_order=orders)

        return orders

    def get_gender(self,order):
        if not order.gender:
            return 'M'

    def get_services(self,order):
        services = self.context['request'].data.get('service')
        names = ''
        for service in services:
            this_service = str(serviceList.objects.filter(id=service).get())
            names = names+' , '+ this_service
        return names
