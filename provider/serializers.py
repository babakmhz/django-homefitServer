
from rest_framework import serializers
from provider.models import provider, services, availableDates
from client.models import subServiceCategory as client_subC
from client.models import serviceDate, serviceTime, availableDateTimeService
from rest_framework import exceptions
from client import Utils

from provider.models import services as serivceModel


class getProvidersSerlizer(serializers.ModelSerializer):

    # total_cost = serializers.SerializerMethodField('get_cost')
    # providing_services = providingServicesSerializer(many=True)
    total_cost = serializers.SerializerMethodField('get_totalCost')

    class Meta:
        model = provider
        fields = ('id', 'name', 'total_cost', 'profile_photo')
        read_only_fields = ('total_cost', )

    def get_totalCost(self, provider):
        request = self.context['request']
        this_services = Utils.appUtils.resolveArrayToList(
            request.GET['services'])
        # TODO: remove 500 error from this section
        total_cost = 0
        cost = 0
        for service in this_services:

            title = client_subC.objects.filter(
                pk=service).values_list('title', flat=True).get()
            cost = services.objects.filter(
                provider__name=provider, name__title=title).values_list('price', flat=True).get()
            total_cost = float(total_cost)+float(cost)

        return total_cost


class dateSerializer(serializers.ModelSerializer):
    class Meta:
        model = serviceDate
        fields = ('id', '_date',)


class timeSerializer(serializers.ModelSerializer):
    class Meta:
        model = serviceTime
        fields = ('id', '_time',)


class dateTimeSerializer(serializers.ModelSerializer):
    date = dateSerializer(many=False)
    time = timeSerializer(many=False)

    class Meta:
        model = availableDateTimeService
        fields = ('date', 'time')


class availableProvidersDate(serializers.ModelSerializer):
    dates = dateTimeSerializer(many=True)

    class Meta:
        model = availableDates
        fields = ('dates',)
