from django.conf.urls import url
from . import views

app_name = 'project'

urlpatterns = [
    url(r'^$',views.ProjectIndexView.as_view(),name='index'),
    url(r'^create/',views.ProjectCreateView.as_view(),name='create'),
    url(r'^list/$',views.ProjectListView.as_view(),name='list'),
    url(r'^delete/project/(?P<pk>\d+)/$',views.ProjectDeleteView.as_view(),name='delete_project'),
    url(r'^delete/certification/(?P<pk>\d+)/$',views.CertificationDeleteView.as_view(),name='delete_cert'),
    url(r'^edit_project/(?P<pk>\d+)/$',views.ProjectUpdateView.as_view(),name='edit_project'),
    url(r'^edit_cert/(?P<pk>\d+)/$',views.CertUpdateView.as_view(),name='edit_cert'),

]