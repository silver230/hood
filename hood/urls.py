from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.hood,name='hood'),
    url(r'^post',views.new_neighbour,name='new_neighbour'),
    url(r'^business/(?P<pk>\d+)/$',views.new_business,name='new_business'),
    url(r'^show/(?P<neighbourhoud_id>\d+)/$', views.show, name='show'), 
    url(r'^search/$',views.search , name='search'),
    url(r'^search_business/$',views.search , name='search_business'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)