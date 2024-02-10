
from django.urls import include, path
from api.views import CompanyViewSet,MachineViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'machines',MachineViewSet)
urlpatterns = [

    path('',include(router.urls))
    
]
