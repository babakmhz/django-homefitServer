"""jick_saniye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from client import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    url(r'^register/$', views.register_or_get_token, name='register'),
    url(r'^sliders/$', views.getSliders.as_view()),
    url(r'^serviceCategories/$', views.getServices.as_view()),
    url(r'^availableServiceDate/$', views.getAvailableServiceDates.as_view()),


    
    # url(r'^submitOrder/$', views.submitOrder.as_view()),
    # TODO: encrypt media directory
    # TODO: change update profile process ----> get token in POST body or HEADER
    # url(r'^uploadClientProfilePhoto/(?P<token__token>[0-9A-Za-z]+)/$',
    #     views.uploadClientProfilePhoto.as_view()),
    # url(r'^uploadClientIdCardPhoto/(?P<token__token>[0-9A-Za-z]+)/$',
    #     views.uploadClientIdCardPhoto.as_view()),
    #url('^profile/(?P<token>.+)/$', views.getClientProfile.as_view()),
]
