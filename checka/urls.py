from django.conf.urls import include,url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checks/$', views.checks, name='checks'),
    url(r'^checks/(?P<check_id>\d+)/$', views.check, name='check'),
    url(r'^checks/new_check/$', views.new_check, name='new_check'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
