
from rest_framework import authentication
from rest_framework import exceptions
from client.models import user,token
from provider.models import provider
class basicAuth(authentication.BaseAuthentication):
    def authenticate(self,request):
        this_token = request.META.get('HTTP_AUTH')

        #print(this_token)
        if this_token == None:
            #print('this_token : '+this_token)
            raise exceptions.AuthenticationFailed('No authority provided')
        try:
            this_user = token.objects.get(token='{}'.format(this_token))
        except user.DoesNotExist:
            raise exceptions.AuthenticationFailed('no credentials provided')
        #print('this user is :'+this_user)
        return (this_user,None)

class providerAuth(authentication.BaseAuthentication):
    def authenticate(self,request):
        personel_id = request.META.get('HTTP_PERSONELID')
        print(personel_id)
        if personel_id == None:
            raise exceptions.AuthenticationFailed('No authority provided')
        try:
            this_personel = provider.objects.get(personel_id__personel_id='{}'.format(personel_id))
        except user.DoesNotExist:
            raise exceptions.AuthenticationFailed('no credentials provided')
            #print('this user is :'+this_user)
            return (this_personel,None)
