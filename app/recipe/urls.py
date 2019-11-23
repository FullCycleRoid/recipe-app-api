from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tag', views.TagViewSet)

ap_name = 'recipe'

urlpatterns = [
    url('', include(router.urls))
]