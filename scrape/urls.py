from django.urls import path
from .import views
from .views import get_jobs





urlpatterns = [
    path('jobs/', views.get_jobs, name='scrape'),
    # path('glassdoor/', views.scrape_glassdoor, name='scrape-glassdoor'),
]