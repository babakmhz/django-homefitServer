from json import JSONEncoder
from uuid import uuid4
from rest_framework import exceptions
from client.clientAuthentication import basicAuth
from client.models import (bannerSlider,
                           serviceCategory,
                           token,
                           availableDateTimeService,
                           order,)
from client.serializers import (bannerSliderSerializer,
                                serviceCategoriesSerializer,
                                submitOrderSerializer,
                                completeOrderSerializer,
                                )
from provider.serializers import getProvidersSerlizer, availableProvidersDate


from provider.models import provider, availableDates
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response
from client import Utils
from client.models import user

# Create your views here.


@csrf_exempt
def register_or_get_token(request):
    # TODO: validate phone_number , restrict robots to create serveral users
    if request.method == 'POST':
        phone = request.POST['phone']
        try:
            this_user = user.objects.filter(phone_number=phone)
            print(this_user.values_list("token__token").get())
            print(phone)
            return JsonResponse({
                'token': '{}'.format(this_user.values_list("token__token", flat=True).get())
            }, encoder=JSONEncoder)
        except user.DoesNotExist:
            new_strtoken = uuid4().hex
            # print(new_strtoken)
            new_token = token.objects.create(token=new_strtoken)
            # print(new_token.objects.values_list("token",flat=True))
            user.objects.create(phone_number=phone, token=new_token)
            return JsonResponse({
                'token': '{}'.format(new_strtoken)
            }, encoder=JSONEncoder)
    else:
        return JsonResponse({
            'result': 'invalid reuqest'
        }, encoder=JSONEncoder)


class getServices(generics.ListAPIView):
    queryset = serviceCategory.objects.all()
    serializer_class = serviceCategoriesSerializer
    authentication_classes = (basicAuth,)


class getSliders(generics.ListAPIView):
    queryset = bannerSlider.objects.all()
    serializer_class = bannerSliderSerializer
    authentication_classes = (basicAuth,)


class getAvailableServiceDates(generics.ListAPIView):
    authentication_classes = (basicAuth,)
    serializer_class = availableProvidersDate

    def get_queryset(self):
        try:
            this_provider = self.request.GET['id']
            return availableDates.objects.filter(provider='{}'.format(this_provider))
        except:
            raise exceptions.APIException('bad request')


class getProviders(generics.ListAPIView):
    serializer_class = getProvidersSerlizer
    authentication_classes = (basicAuth,)

    def get_queryset(self):
        try:
            this_services = self.request.GET['services']
            this_category = self.request.GET['category']
            querySet = None
            services = Utils.appUtils.resolveArrayToList(this_services)
            print('services in views:', services)
            services.sort(reverse=True)
            for j in services:
                querySet = provider.objects.filter(
                    providing_category__id=this_category, providing_services__id=j)
            print('queryset is : ',querySet)
            return querySet
        except:
            raise exceptions.APIException('bad request')


class submitOrder(generics.CreateAPIView):
    serializer_class = submitOrderSerializer
    authentication_classes = (basicAuth,)

    def get_queryset(self):
        return order.objects.all()


class compeleteOrder(generics.RetrieveUpdateAPIView):
    serializer_class = completeOrderSerializer
    lookup_field = 'orderNumber'
    queryset = order.objects.all()
    authentication_classes = (basicAuth,)
