from django.contrib import admin
from .models import Apply_contact
# Register your models here.
@admin.register(Apply_contact)
class Apply_contactAdmin(admin.ModelAdmin):
    list_display=['name','mail']