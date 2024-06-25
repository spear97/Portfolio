from django.urls import path
from landing import views as landing_views
from aptdb import views as apt_views
from sentimentanalysis import views as sent_views

urlpatterns = [
    path('', landing_views.home, name='home'),
    path('aptdb/', apt_views.index, name='aptdb'),
    path('aptdb/get_apartments/', apt_views.search, name='aptdb_results'),
    path('sentiment_analysis/', sent_views.index, name='sent_index'),
    path('sentiment_analysis/analysis/', sent_views.sentiment_analysis, name='analysis')
]
