from django.contrib import admin
from .models import Job,Apply
# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['job_name','place','salary','type_job','vacancy']

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display=['name','mail']