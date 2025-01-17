from operator import index
from tkinter.font import names

from django.shortcuts import render

from CVGenerator.models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import  loader



# Create your views here.
def home(request):
    return render(request,'index.html')

from django.shortcuts import render, redirect
from .models import Profile

def accept(request):
    if request.method == "POST":  # Corrected "POST" case
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")  # Removed extra space
        skills = request.POST.get("skill", "")

        # Save data to the database
        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills
        )
        profile.save()



    # If method is GET, show the form
    return render(request, 'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    return render(request,'pdf/resume.html',{'user_profile':user_profile})

