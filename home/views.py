from django.shortcuts import render
from joobs.models import Job
from contact.models import Apply_contact
from .forms import SearchForm
# Create your views here.
def home(request):
    job=Job.objects.all()[:4]
    cont=Apply_contact.objects.all()[:4]
    context={
        'job':job,
        'cont':cont
    }
    return render(request,'Home/home.html',context)