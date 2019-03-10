from django.conf.urls import url

from .views import display_slides, add_slides, slide_details, user_slides


urlpatterns = [
    url(r'^view-slides/$', display_slides, name='view'),
    url(r'^my-slides/$', user_slides, name='user_sld'),
    url(r'^slide-details/(?P<slug>[\w-]+)/$', slide_details, name='details'),
    url(r'^add/$', add_slides, name='add'),
]