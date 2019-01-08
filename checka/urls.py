from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checks/$', views.CreateView.as_view(), name="create"),
    url(r'^checks/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
    url(r'^shops/$', views.CreateShopView.as_view(), name="create"),
    url(r'^shops/(?P<pk>[0-9]+)/$', views.DetailsShopView.as_view(), name="details"),
    # url(r'^checks/$', views.checks, name='checks'),
    # url(r'^checks/(?P<check_id>\d+)/$', views.check, name='check'),
    # url(r'^checks/new_check/$', views.new_check, name='new_check'),
    # url(r'^checks/edit_check/(?P<check_id>\d+)/$', views.edit_check, name='edit_check'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
