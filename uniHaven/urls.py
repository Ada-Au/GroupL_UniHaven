from django.urls import path
from uniHaven import views

urlpatterns = [
    path('hello', views.hello),
    path('accommodation_list', views.accommodation_list),
]