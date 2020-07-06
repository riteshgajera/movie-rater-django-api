from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from movierater import settings
from .views import MovieViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
