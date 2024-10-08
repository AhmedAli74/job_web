from django.shortcuts import render,redirect
from .models import Apply_contact
# Create your views here.
def contact(request):
    if request.method=='POST':
        nm=request.POST['name']
        email=request.POST['email']
        subjects=request.POST['subject']
        message=request.POST['message']
        test=Apply_contact()
        test.name=nm
        test.mail=email
        test.subject=subjects
        test.messages=message
        test.save()
        return redirect('Contact:contact')
    return render(request,'contact/contact.html')