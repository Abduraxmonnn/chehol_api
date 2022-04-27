from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from product.views import CoverViewSet

router = DefaultRouter()
router.register(r'cover', CoverViewSet, 'cover')

urlpatterns = [
    url(r'', include(router.urls)),
]
