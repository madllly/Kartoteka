from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.MainPage.as_view()),
    path('filter/',views.FilterEstateView.as_view(),name='filter'),
    path('test/', views.IndexView.as_view()),
    path('home/',views.index_test),

]

