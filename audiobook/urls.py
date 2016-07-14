from django.conf.urls import url
from . import views
app_name = 'audiobook'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^chapters/(?P<chapter_id>[0-9]+)/$', views.play, name='play'),

    url(r'^chapters/(?P<filter_by>[0-9]+)/$', views.chapters, name='chapters'),
    url(r'^create_book/$', views.create_book, name='create_book'),
    url(r'^(?P<chapter_id>[0-9]+)/create_chapter/$', views.create_chapter, name='create_chapter'),
    url(r'^(?P<book_id>[0-9]+)/delete_chapter/(?P<chapter_id>[0-9]+)/$', views.delete_chapter, name='delete_chapter'),
    url(r'^(?P<book_id>[0-9]+)/delete_book/$', views.delete_book, name='delete_book'),

]
