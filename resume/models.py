from django.db import models


class Job(models.Model):
    job_title = models.CharField(max_length=200)
    job_company = models.CharField(max_length=50)
    job_picture = models.ImageField(upload_to='job_image', blank=True)
    job_desc = models.TextField()
    job_start_date = models.DateField('date started')
    job_end_date = models.DateField('date ended')

    # class Meta:
    #     app_label = 'Resume'

    def __str__(self):
        return self.job_title

# class Project(models.Model):
#
#
# class Overview(models.Model):
#
#
# class Education(models.Model):
#
#
# class Hobby(models.Model):
#
#
# class Skill(models.Model):


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, help_text="e.g. city such as Boston")
    state = models.CharField(max_length=2, help_text="e.g. state such as MA")
    email = models.EmailField()
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Personal Info"

    def full_name(self):
        return " ".join([self.first_name, self.last_name])

    def __unicode__(self):
        return self.full_name()