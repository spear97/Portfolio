from django.urls import path
from landing import views as landing_views

urlpatterns = [
    path('', landing_views.home, name='home'),
]
