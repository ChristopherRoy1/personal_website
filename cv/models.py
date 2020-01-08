from django.db import models

# Create your models here.

#class SkillItemType(models.Model):


#class SkillItem(models.Model):




class EducationItem(models.Model):
    education_item_title = models.CharField(max_length=100)
    education_item_level = models.CharField(max_length=100, default="")
    education_item_start_date = models.DateField(auto_now=True)
    education_item_end_date = models.DateField(auto_now=True)
    education_item_institution = models.CharField(max_length=100, default="")


class WorkItem(models.Model):
    work_item_position_title = models.CharField(max_length=100)
    work_item_department = models.CharField(default="", null=True, max_length=100)
    work_item_company = models.CharField(max_length=100)
    work_item_start_date = models.DateField(auto_now=True)
    work_item_end_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.work_item_position_title + " company: " + self.work_item_company

class WorkItemBullet(models.Model):
    work_item = models.ForeignKey(WorkItem, on_delete=models.CASCADE)
    work_item_bullet = models.CharField(max_length=100)
