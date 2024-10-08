from django.urls import path
from landing import views as landing_views
from aptdb import views as apt_views

urlpatterns = [
    path('', landing_views.home, name='home'),
    path('aptdb/', apt_views.index, name='aptdb'),
    path('aptdb/get_apartments/', apt_views.search, name='aptdb_results'),
    path('currency_converter/', landing_views.currency_converter, name='currency_converter'),
    path('FlightForceCalculator/', landing_views.Flight_Force_Calculator, name='flight_force')
]
