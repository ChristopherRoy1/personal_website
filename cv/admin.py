from django.contrib import admin
from cv.models import EducationItem, WorkItem, WorkItemBullet
# Register your models here.
admin.site.register(EducationItem)
admin.site.register(WorkItem)
admin.site.register(WorkItemBullet)
