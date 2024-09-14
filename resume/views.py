from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render (request,"home.html")
def about(request):
    return render (request,"about.html")
def projects(request):
    projects_show = [
        {
            "title":"CGPA Calculator Web Application",
            "path":"images/CGPA.png"
        },
        {
            "title":"Innovative Visions: Greeshmanth's Portfolio",
            "path":"images/portfolio.PNG"
        },

    ]
    return render (request,"projects.html",{"projects_show":projects_show})
def certificates(request):
    return render (request,"certificates.html")
def contact(request):
    return render (request,"contact.html")
def resume(request):
    resume_path="resumepdf/2301050196_Greeshmanth.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(),content_type="application/pdf")
            response['content-Disposition']='attachment';filename="2301050196_Greeshmanth.pdf"
            return response
    else:
        return HttpResponse("Resume not found", status=404)