from rest_framework import routers
from  TODO import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'task', views.TaskModelViewsSet, basename='task')


urlpatterns = [
    path('', include(router.urls)),
]
