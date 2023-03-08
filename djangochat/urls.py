from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    # path('pv/', include('private.urls')),
    path('admin/', admin.site.urls),
]
