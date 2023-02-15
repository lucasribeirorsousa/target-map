from django.urls import path
from .views import home, add_target

urlpatterns = [
    path('home/', home, name='home'),
    path('add_target/', add_target, name='add_target'),
]