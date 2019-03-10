from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from slides.views import display_slides, add_slides, slide_details
from users.views import register 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^slides/', include('slides.urls')),
    url(r'^/', include('users.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)