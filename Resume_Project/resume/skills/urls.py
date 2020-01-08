from django.conf.urls import url,include
from skills import views

app_name = 'skills'

urlpatterns = [
    url(r'^index/',views.SkillsIndexView.as_view(),name='index'),
    url(r'^create/$',views.SkillsCreateView.as_view(),name='create'),
    url(r'^list/$',views.SkillListView.as_view(),name='list'),
    url(r'^delete/(?P<pk>\d+)/$',views.SkillDeleteView.as_view(),name='delete'),
    url(r'^update/(?P<pk>\d+)/$',views.SkillUpdateView.as_view(),name='update'),
]