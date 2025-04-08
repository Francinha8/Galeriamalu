from django.contrib import admin
from .models import Photo, Upload

admin.site.register(Upload)
admin.site.register(Photo)