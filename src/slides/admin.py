from django.contrib import admin


from .models import Slide, SlideUpload

admin.site.register(Slide)
admin.site.register(SlideUpload)