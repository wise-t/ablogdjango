
from django.urls import path
from .views import UserRegisterViews
#rom.import views

urlpatterns = [
    path('register/',UserRegisterViews.as_view(),name='register'),

]