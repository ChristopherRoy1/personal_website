from django.db import models

# Create your models here.

#class SkillItemType(models.Model):


#class SkillItem(models.Model):




class EducationItem(models.Model):
    education_item_title = models.CharField(max_length=100)
    education_item_level = models.CharField(max_length=100, default="")
    education_item_start_date = models.DateField(auto_now=False)
    education_item_end_date = models.DateField(auto_now=False,null=True, blank=True)
    education_item_institution = models.CharField(max_length=100, default="")

    def __str__(self):
        tostr = "[" + self.education_item_title + "][" + \
        self.education_item_level + "][" + \
        self.education_item_institution + "]"

        return tostr

class WorkItem(models.Model):
    work_item_position_title = models.CharField(max_length=100)
    work_item_department = models.CharField(default="", null=True, max_length=100)
    work_item_company = models.CharField(max_length=100)
    work_item_start_date = models.DateField(auto_now=False)
    work_item_end_date = models.DateField(auto_now=False, null=True, blank=True)

    @property
    def get_bullets(self):
        return WorkItemBullet.objects.filter(work_item=self).order_by('work_item_ordering')

    def __str__(self):
        tostr = "[" + self.work_item_company + "][" + \
                      self.work_item_position_title + "][" + \
                      self.work_item_department + "]"
        return tostr



class WorkItemBullet(models.Model):

    work_item = models.ForeignKey(WorkItem, on_delete=models.CASCADE)
    work_item_bullet = models.TextField()
    work_item_finished = models.BooleanField(default=False)
    work_item_ordering = models.IntegerField()

    def __str__(self):
        tostr = "[" + str(self.work_item) + "][" + \
        (str(self.work_item_bullet))[:100] + "][" + \
        str(self.work_item_finished) + "]"

        return tostr

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['work_item_ordering', 'work_item_finished'], name='ordering constraint'),
            models.UniqueConstraint(fields=['work_item', 'work_item_bullet', 'work_item_finished'], name="duplicate bullet constraint")
        ]
