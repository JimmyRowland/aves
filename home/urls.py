from django.conf.urls import url
from . import views
app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^audio/$', views.audio, name='audio'),
    url(r'^schedules/$', views.schedules, name='schedules'),
]
