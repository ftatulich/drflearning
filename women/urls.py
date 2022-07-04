from django.urls import path, include
from rest_framework import routers

from women.views import WomenViewSet

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)

urlpatterns = [
    path('', include(router.urls))
]
