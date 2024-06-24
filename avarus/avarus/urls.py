"""
URL configuration for avarus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from avarus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('services/', views.ServicesView, name='services'),
    path('publications/', include('apps.publications.urls')),
    path('statistics/', include('apps.statistics.urls')),
    path('authors/', include('apps.authors.urls')),
    path('datasets/', include('apps.datasets.urls')),
    path('related-projects/', include('apps.related_projects.urls')),
    path('', include('apps.profiles.urls')),
    path('', include('apps.feedback.urls')),
    prefix_default_language=False
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL + 'datasets/img/', document_root=settings.MEDIA_ROOT + '/datasets/img')
urlpatterns += static(settings.MEDIA_URL + 'tmp/', document_root=settings.MEDIA_ROOT + '/tmp')
