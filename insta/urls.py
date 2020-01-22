from django.urls import path
from django.conf.urls import url, include
from .views import HomePageView, Names

urlpatterns = [
          
              path('', HomePageView.as_view(), name='home'),
              path('namesu/', Names.as_view(), name='namesus'),
              url(r'^submit', HomePageView.submit),
              

]