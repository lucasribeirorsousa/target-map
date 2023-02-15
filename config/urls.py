from django.contrib import admin
from django.urls import path, include
from apps.targets.views import home, add_target

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.targets.urls')),
]
