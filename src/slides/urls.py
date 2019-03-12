from django.conf.urls import url

from .views import display_slides, add_slides, user_slides, delete_slide


urlpatterns = [
    url(r'^$', display_slides, name='view'),
    url(r'^my-slides/$', user_slides, name='user_sld'),
    url(r'^add/$', add_slides, name='add'),
    url(r'^delete/(?P<pk>\d+)/$', delete_slide, name='delete'),
]