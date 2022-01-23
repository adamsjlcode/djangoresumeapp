from django.contrib import admin
from django.utils.html import mark_safe

from resume.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_company')
    readonly_fields = ["job_image"]

    def job_image(self, obj):
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.job_picture.url,
                width=obj.job_picture.width,
                height=obj.job_picture.height,
        )
    )