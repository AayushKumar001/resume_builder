from django.conf.urls import url,include
from . import views

app_name = 'summary'

urlpatterns = [
    url(r'^$',views.SummaryIndexView.as_view(),name='index'),
    url(r'^create/$',views.SummaryCreateView.as_view(),name='create'),
]