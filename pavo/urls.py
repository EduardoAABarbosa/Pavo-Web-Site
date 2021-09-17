"""pavo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.api import viewsets

router=routers.SimpleRouter()
router.register(r'cadastro_depoimentos',viewsets.DepoimentosViewSet)

router2=routers.SimpleRouter()
router2.register(r'cadastro_redes_sociais',viewsets.Redes_SociaisViewSet)

router3=routers.SimpleRouter()
router3.register(r'cadastro_downloads',viewsets.DownloadsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('article',include('core.urls')),
    path('privact',include('core.urls')),
    path('terms',include('core.urls')),
    path('',include(router.urls)),
    path('',include(router2.urls)),
    path('',include(router3.urls)),
]
