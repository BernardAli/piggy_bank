
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'categories', views.CategoryModelViewSet, basename="category")
router.register(r'transactions', views.TransactionModelViewSet, basename="transaction")

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_auth_token, name="obtain-auth-token"),
    path("admin/", admin.site.urls),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
    path("report/", views.TransactionReportAPIView.as_view(), name="report"),
    path('__debug__/', include('debug_toolbar.urls')),
] + router.urls
