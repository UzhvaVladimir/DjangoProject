from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about',views.about, name='about'),
    path('create',views.create, name='create'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
