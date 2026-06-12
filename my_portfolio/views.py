from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Project
from django.contrib.auth.decorators import login_required

# Ithu nalkiyaal login cheyyatha aalukalkku ee page kaanan pattilla

def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio.html", {"projects": projects})

def login_page(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            login(request, user)

            # ✅ THIS IS CORRECT FLOW
            return redirect(request.GET.get('next') or 'addproject')

        return render(request, 'login.html', {'error': 'Invalid login'})

    return render(request, 'login.html')





@login_required(login_url='/login/')
def projectadd(request):
    if request.method == "POST":
        Project.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            github_link=request.POST.get("github_link"),
        )
        return redirect("home")

    return render(request, "projectadd.html")