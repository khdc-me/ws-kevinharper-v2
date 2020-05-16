from django.urls import path

from .views import ExperiencePageView, HomePageView


urlpatterns = [
    path('experience', ExperiencePageView.as_view(), name='experience'),
    path('', HomePageView.as_view(), name='home'),
]
