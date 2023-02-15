from django.contrib import admin
from django.urls import path
from apps.targets.views import home, add_target

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_target/', add_target, name='add_target'),
]
