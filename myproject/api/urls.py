from django.contrib import admin
from django.urls import path,include
from api.views import DepartmentViewSet,EmployeeViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [    
    path('',include(router.urls)) 
]

