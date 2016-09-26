"""zxk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    #url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    #url(r'^account/', include('account.urls')),  # 使用Django自带试图的话就别加namespace了
    #url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^github/', include('github.urls', namespace='github')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)