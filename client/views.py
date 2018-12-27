from json import JSONEncoder
from uuid import uuid4
from rest_framework import exceptions
from client.clientAuthentication import basicAuth
from client.models import (bannerSlider,
                                          serviceCategory,
                                           token,
                                            user,
                                            order,
                                            service,
                                            service_tip)
from client.serializers import (bannerSliderSerializer,
                                serviceCategoriesSerializer
                                , userSerializer,
                                updateUserSerializer,
                                submitOrderSerializer,
                                servicesSerializer,
                                profilePhotoSerializer,
                                IdCardPhotoSerializer,
                                getUserSerializer,
                                serviceTipSerializer,
                                )

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response



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
                'token': '{}'.format(this_user.values_list("token__token",flat=True).get())
            }, encoder=JSONEncoder)
        except user.DoesNotExist:
            new_strtoken = uuid4().hex
            print(new_strtoken)
            new_token = token.objects.create(token=new_strtoken)
            #print(new_token.objects.values_list("token",flat=True))
            user.objects.create(phone_number=phone,token=new_token)
            return JsonResponse({
            'token':'{}'.format(new_strtoken)
            },encoder=JSONEncoder)
    else:
        return JsonResponse({
        'result':'invalid reuqest'
        },encoder=JSONEncoder)


class getServices(generics.ListAPIView):
    queryset = serviceCategory.objects.all()
    serializer_class = serviceCategoriesSerializer
    authentication_classes = (basicAuth,)

class getSliders(generics.ListAPIView):
    queryset = bannerSlider.objects.all()
    serializer_class = bannerSliderSerializer
    authentication_classes = (basicAuth,)

class getClientProfile(generics.ListAPIView):
    serializer_class = getUserSerializer
    authentication_classes = (basicAuth,)
    def get_queryset(self):
        this_token = self.request.GET['token']
        print(this_token)
        return user.objects.filter(token__token = '{}'.format(this_token))

class updateClientProfile(generics.UpdateAPIView):
    serializer_class = updateUserSerializer
    ## TODO: create permission that only this user can change information
    queryset = user.objects.all()
    authentication_classes = (basicAuth,)
    lookup_field = 'token__token'

class submitOrder(generics.CreateAPIView):
    serializer_class = submitOrderSerializer
    authentication_classes = (basicAuth,)
    queryset = order.objects.all()

class getServicesDetail(generics.ListAPIView):
    serializer_class = servicesSerializer
    authentication_classes = (basicAuth,)
    def get_queryset(self):
        #print(self.request.GET['category'])
        try:
            this_category = self.request.GET['category']
            return service.objects.filter(category__id=this_category)
        except:
            raise exceptions.APIException('bad request')

class uploadClientProfilePhoto(generics.RetrieveUpdateAPIView):
    authentication_classes = (basicAuth,)
    serializer_class = profilePhotoSerializer
    queryset = user.objects.all()
    lookup_field = 'token__token'


class uploadClientIdCardPhoto(generics.RetrieveUpdateAPIView):
    authentication_classes = (basicAuth,)
    serializer_class = IdCardPhotoSerializer
    queryset = user.objects.all()
    lookup_field = 'token__token'

class getServicesDetailAll(generics.ListAPIView):
    serializer_class = servicesSerializer
    authentication_classes = (basicAuth,)
    queryset = service.objects.all()

class getServiceTip(generics.ListAPIView):
    serializer_class = serviceTipSerializer
    authentication_classes = (basicAuth,)
    def get_queryset(self):
        try:
            this_service = self.request.GET['id']
            return service_tip.objects.filter(service__id=this_service)
        except:
            raise exceptions.APIException('bad request')
