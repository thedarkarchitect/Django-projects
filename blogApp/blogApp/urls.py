"""blogApp URL Configuration

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
from core.views import frontpage, about,robots_txt
from django.conf.urls.static import static
from django.conf import settings
#sitemaps imports
from django.contrib.sitemaps.views import sitemap
from blogApp.sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category':CategorySitemap, 'post':PostSitemap}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('about/', about, name='about'),
    path('', include('blog.urls')),
    path('', frontpage, name='frontpage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
