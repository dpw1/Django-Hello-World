from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^$', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]
