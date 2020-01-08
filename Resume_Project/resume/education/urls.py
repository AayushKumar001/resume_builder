from django.conf.urls import url,include
from . import views

app_name = 'education'

urlpatterns = [
    url(r'form/$',views.EducationCreateView.as_view(),name='create'),
    url(r'list/schools/$',views.EducationListView.as_view(),name='list'),
    url(r'^delete/(?P<pk>\d+)/$',views.EducationDeleteView.as_view(),name='delete'),
    url(r'^update/(?P<pk>\d+)/$',views.EducationUpdateView.as_view(),name='update'),
    url(r'^skills/',include('skills.urls',namespace='skills')),
    
    
]