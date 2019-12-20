from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^about/',views.AboutView.as_view(),name='about'),
    url(r'^listings/',include('listings.urls',namespace='listings')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^contacts/',include('contacts.urls',namespace='contacts')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
