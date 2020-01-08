from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'personal_info'

urlpatterns = [
    url(r'^resume/address/',views.PersonalContactInfoView.as_view(),name='address'),
    url(r'^experience/',include('experience.urls',namespace='experience'))
]

