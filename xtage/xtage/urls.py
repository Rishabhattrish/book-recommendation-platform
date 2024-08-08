from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  app.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
# urls.py
# router.register(r'comments', CommentViewSet)
# router.register(r'likes', LikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Book API",
      default_version='v1',
      description="API for managing book recommendations",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
