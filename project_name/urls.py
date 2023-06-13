"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import logout_then_login
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from {{ project_name }} import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", logout_then_login, name="logout"),
    path("userextensions/", include("userextensions.urls")),
    path("handyhelpers/", include("handyhelpers.urls")),
    path("hostutils/", include("djangoaddicts.hostutils.urls")),
    # API documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # local apps
    path("", views.Index.as_view(), name="index"),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)
