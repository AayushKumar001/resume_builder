from django.conf.urls import url,include
from experience import views

app_name = 'experience'

urlpatterns = [
    url(r'^user/(?P<slug>[-\w]+)/$',views.ExperienceIndexView.as_view(),name='experience_index'),
    url(r'^create/',views.ExperienceCreateView.as_view(),name='create'),
    url(r'^experience/(?P<pk>\d+)/$',views.ExperienceDetailView.as_view(),name='detail'),
    #url(r'^list/(?P<pk>[-\w]+)/$',views.ExperienceListView.as_view(),name='list'),
    url(r'^list/$',views.ExperienceListView.as_view(),name='list'),
    url(r'^education/',include('education.urls',namespace='education')),
    url(r'^update/(?P<pk>\d+)/$',views.ExperienceUpdateView.as_view(),name='exp_edit'),
    url(r'^delete/(?P<pk>\d+)/$',views.ExperienceDeleteView.as_view(),name='delete'),
]
    #url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
