from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Project

# Ithu nalkiyaal login cheyyatha aalukalkku ee page kaanan pattilla

def home(request):
    # Database-il ulla ellaa projects-um edukkunnu
    projects = Project.objects.all() 
    # 'projects' enna peril template-ilekku ayakkunnu
    return render(request, 'portfolio.html', {'projects': projects})

def login_page(request):
    if request.method =='POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request,username=u, password=p)
        if user is not None:
            login(request, user)
        return redirect('addproject')
    else:
        return render(request, 'login.html')
def AddProject(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        img=request.FILES.get('imge_field_name')
        # Database-lekku save cheyyunnu
        new_project = Project(title=title, description=desc,imge=img)
        new_project.save()
        
        return redirect('home') # Save ayal home page-lekku povan
    
    return render(request, 'projectadd.html')