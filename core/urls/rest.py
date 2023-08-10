from django.urls import path
from django.conf.urls import include
from rest_framework import routers

app_name = 'rest'

router = routers.DefaultRouter()


urlpatterns = [

    # API views
    path('', include(router.urls)),
    path('v1/', include(router.urls)),

]
