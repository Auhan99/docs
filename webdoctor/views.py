from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from suraj.settings import LOGIN_URL
from django.shortcuts import get_object_or_404

def home(request):
    categories= categorie.objects.all()
    context = {
        'categories': categories,
    }
    return render(request,"index.html",context)

def details(request,pk):
    doc=get_object_or_404(doctor,id=pk)
    return render(request,'detail-page.html',context={'doctor':doc,})


def form(request):
    template_name = 'login.html'
    logout(request)
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        if request.method == 'POST':
            post = request.POST
            email = post.get('email', None)
            password = post.get('pass1', None)
            # print(email, password)
            if password and email:
                try:
                    userprofile = UserProfile.objects.get(email=email)
                except:
                    return HttpResponse('No user found')

                userprofile = authenticate(email=email, password=password)
                if userprofile:
                    userprofile.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, userprofile)
                    return redirect('/')
                else:
                    return HttpResponse('wrong password')
        else:
            return render(request, template_name)
    else:
        print("already")
        return redirect('/')


@login_required(login_url=LOGIN_URL)
def search(request):
    if request.method=="GET":
        data=request.GET
        category=data.get('search',None)
        category=category.replace(' ','')

        doctors = doctor.objects.filter(category__category__iregex=category)

        context={
            'doctors':doctors,
            'categories':categorie,
            'doctorname':category,
                  }
        return render(request,'list.html',context)

@login_required(login_url=LOGIN_URL)
def bookDoctor(request,pk):
    doc=get_object_or_404(doctor,id=pk)
    # print(request.user.email)
    return render(request,'booking-page.html',context={'doctor':doc,})

def register(request):
    if request.method=='POST':
        post=request.POST
        email=post.get('email',None)
        name=post.get('name',None)
        password=post.get('pass',None)
        userprofile=UserProfile.objects.create(name=name,email=email)
        userprofile.set_password(password)
        userprofile.save()
        return HttpResponse('success')

