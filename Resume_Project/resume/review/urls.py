from django.conf.urls import url,include
from . import views

app_name = 'review'

urlpatterns = [
    url(r'^list/$',views.ReviewList.as_view(),name='list'),
    url(r'^generate/$',views.GeneratePdf.as_view(),name='generate'),
    url(r'^pdf/',views.index,name='index')

]