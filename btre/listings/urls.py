from django.conf.urls import url
from . import views
app_name = 'listings'

urlpatterns = [
    url(r'^$',views.ListingIndexView.as_view(),name='listings'),
    url(r'^list/(?P<pk>[-\w]+)/$',views.ListingDetailView.as_view(),name='detail'),
    url(r'^search/',views.Search.as_view(),name='search'),
]