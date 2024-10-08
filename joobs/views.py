from django.http import Http404
from django.shortcuts import render,redirect
from .models import Job,Apply
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def job(request):
    jobs=Job.objects.all()
    paginator = Paginator(jobs, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'jobs':page_obj
    }
    return render(request,'jobs/job_list.html',context)

def job_details(request,job_slug):
    try:
        job_detail = Job.objects.get(slug=job_slug)
    except Job.DoesNotExist:
        raise Http404("Job not found")
    
    if request.method=='POST':
        nm=request.POST['name']
        email=request.POST['email']
        website=request.POST['Web_site']
        cV=request.FILES['cv']
        cover=request.POST['cover']
        data=Apply()
        data.name=nm
        data.mail=email
        data.web=website
        data.cv=cV
        data.cover=cover
        data.job=job_detail
        data.save()
        redirect('Job:jobs')

    context={
        'job_detail':job_detail
    }
    return render(request,'jobs/job_details.html',context)

@login_required(login_url='accounts:login')
def add_job(request):
    if request.method=='POST':
        names=request.POST['name']
        img=request.FILES['image']
        plc=request.POST['place']
        type_job=request.POST['job_type']
        salary=request.POST['salary']
        vac=request.POST['vacancy']
        desc=request.POST['description']
        qualification=request.POST['qualifications']
        form=Job()
        form.job_name=names
        form.image=img
        form.place=plc
        form.type_job=type_job
        form.salary=salary
        form.vacancy=vac
        form.description=desc
        form.qualifications=qualification
        form.save()
        redirect('Job:jobs')

    return render(request,'jobs/post_job.html')