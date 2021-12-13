from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from products.views import ProductView
from application.views import AcceptedFormView, ApplicationFormDetailView, ApplicationFormView, StatusChangeFormView
from rest_framework import routers


route = routers.DefaultRouter()
route.register("product", ProductView, basename='productview')
route.register("form", ApplicationFormView, basename='applicationformview')
route.register("accepted", AcceptedFormView, basename='acceptedform')
route.register("status", StatusChangeFormView, basename='statuschangeformview')
route.register("form-details", ApplicationFormDetailView, basename='applicationformdetailview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
