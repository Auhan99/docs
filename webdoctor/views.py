from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from suraj.settings import LOGIN_URL
from django.shortcuts import get_object_or_404
from django.core import serializers
from .key import key
import json
from django.http import JsonResponse


# def test(request):
#     pin=PinCode.objects.filter(pin="221005")
#     docs=doctor.objects.filter(pin__in="221005")
#     #aas=PinCode.objects.all().values_list(pin)
#     print(docs)
#     posts_serialized = serializers.serialize('json', docs)
#     return JsonResponse({'doctors':posts_serialized,})

def test(request):
	p=Pos.objects.all()
	print(p)
	return render(request,'maps.html',context={'markers':p,})

def getnear(request,lat,lag):
    url="https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+lag+"&key="+key
    address=request.get(url).json()    ##remove .json() if error pops up
    postal_code=address['results'][0]['address_components'][6]['long_name']
    pin=PinCode.objects.filter(pin=postal_code)
    docs=doctor.objects.filter(pin=pin)
    return JsonResponse({'doctors':docs,key:key})


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

def booked(request, pk):
    if request.method == 'POST':
        post = request.POST
        name = post.get('firstname_booking', None)
        # lastName = post.get('lastname_booking', None)
        phone = post.get('telephone_booking', None)
        age = post.get('Age', None)
        gender = post.get('gender', None)
        docrecord = DocHistory.objects.create(name=name, age=age, gender=gender, phone=phone)
        docrecord.doctorInConcern_id = pk
        docrecord.save()
        return HttpResponse('<div class="jumbotron"><h1>Your Booking Was Successful!!</h1></div>')
        

def history(request, pk):
    history = DocHistory.objects.filter(doctorInConcern__id=pk)
    return render(request, 'dochistory.html', context={'history': history})

