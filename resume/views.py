from django.shortcuts import render
from resume.models import Job


def index(request):
    job_list = Job.objects.order_by('-job_start_date')
    # job_list = Job.objects.all()
    # projects = Project.objects.all()
    # hobbies = Hobby.objects.all()
    # education = Education.objects.all()
    context = {
        'jobs': job_list,
        # 'projects': projects,
        # 'hobbies': hobbies,
        # 'education': education,
        }
    return render(request, 'global/resume.html', context)
