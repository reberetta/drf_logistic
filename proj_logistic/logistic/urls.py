from django.urls import include, path
from rest_framework import routers
from .views import LogisticViewSet

router = routers.DefaultRouter()
router.register(r'logistic', LogisticViewSet, basename="logistic")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]