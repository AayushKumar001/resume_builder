from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^dashboard/$',views.DashboardView.as_view(),name='dashboard'),
    url(r'^logout/',views.logout,name='logout'),
]
