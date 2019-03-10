from django.contrib import admin

# Register your models here.
from .models import Slide, SlideUpload

admin.site.register(Slide)
admin.site.register(SlideUpload)