"""EntregaLezanBlancJimenez URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from comun.views import home_view, about_view

urlpatterns = [
    path('', home_view, name='home'), #poner la vista home de BLOG-pages, cuando esté, para q sea la ruta base
    path('about/', about_view, name='about'), #poner la vista home de BLOG-pages, cuando esté, para q sea la ruta base
    path('admin/', admin.site.urls),
    path('AppEntrega1/', include('AppEntrega1.urls')),
    path('accounts/', include('accounts.urls')),
    path('Blog/', include('Blog.urls')),
    #path('Inicio/', inicio, name='inicio'),
    path('Mensajes/', include('Mensajes.urls')),
    
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)