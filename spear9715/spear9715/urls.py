"""
URL configuration for spear9715 project.

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
import landing.views as land_views
import sentimentanalysis.views as sentiment_views
import aptdb.views as aptdb_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', land_views.index, name='land_index'),
    path('sentimentanalysis/', sentiment_views.index, name='sentiment_index'),
    path('sentimentanalysis/analysis', sentiment_views.sentiment_analysis, name='sentiment_analysis'),
    path('apartmentdatabase/', aptdb_views.index, name='aptdb_index'),
    path('apartmentdatabase/search/', aptdb_views.search, name='aptdb_search')
]
