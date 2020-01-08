from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^about/',views.AboutView.as_view(),name='about'), 
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^create_personal_info/',include('personal_info.urls',namespace='personal_info')),
    url(r'^create_experience/',include('experience.urls',namespace='experience')),
    url(r'^create_education/',include('education.urls',namespace='education')),
    url(r'^create_skills/',include('skills.urls',namespace='skills')),
    url(r'^create_summary/',include('summary.urls',namespace='summary')),
    url(r'^create_project/',include('project.urls',namespace='project')),
    url(r'^create_review/',include('review.urls',namespace='review')),
    url(r'^thanks/',views.ThanksPageView.as_view(),name='thanks'),
    url(r'^test/',views.TestView.as_view(),name='test'),
    url(r'^reports/',views.ReportList.as_view(),name='report'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
