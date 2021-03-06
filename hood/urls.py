from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.hood,name='hood'),
    url(r'^post',views.new_neighbour,name='new_neighbour'),
    url(r'^business/(?P<pk>\d+)',views.new_business,name='new_business'),
    url(r'^show/(\d+)', views.show, name='show'), 
    url(r'^search/$',views.search , name='search'),
    url(r'^search_business/$',views.search , name='search_business'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('edit/',views.edit, name='edit'),
    url( r'^profile/$' , views.profile , name='profile' ),
    url( r'pro/(?P<pk>[0-9]+)/$' , views.dump, name='dump' ),
    url( r'project/(?P<pk>[0-9]+)/$' , views.AlbumUpdate.as_view( ) , name='album-update' ) ,
    url( r'prof/(?P<pk>[0-9]+)/$' , views.ProfileUpdate.as_view( ) , name='profile-update' ) ,
    url( r'project/(?P<pk>[0-9]+)/delete/$' , views.AlbumDelete.as_view( ) , name='album-delete' ) ,
    url( r'profile/(?P<pk>[0-9]+)/delete/$' , views.ProfileDelete.as_view( ) , name='profile-delete' ) ,
    url( r'^create/$' , views.create , name='create' ),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)