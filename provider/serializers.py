
from rest_framework import serializers
from provider.models import provider, services
from client.models import subServiceCategory as client_subC
from rest_framework import exceptions
from client import Utils


class getProvidersSerlizer(serializers.ModelSerializer):

    # total_cost = serializers.SerializerMethodField('get_cost')
    # providing_services = providingServicesSerializer(many=True)
    total_cost = serializers.SerializerMethodField('get_totalCost')

    class Meta:
        model = provider
        fields = ('name', 'total_cost')
        read_only_fields = ('total_cost', )

    def get_totalCost(self, provider):
        request = self.context['request']
        this_services = Utils.appUtils.resolveArrayToList(
            request.GET['services'])
        total_cost = 0
        for service in this_services:
            try:
                title = client_subC.objects.filter(
                    pk=service).values_list('title', flat=True).get()
                print(title)
                trycost = services.objects.filter(
                    provider__name=provider, name__title=title).values_list('price', flat=True).get()
                total_cost = float(total_cost)+float(cost)
                return total_cost
            except :
                return None