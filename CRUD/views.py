from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_information
# Create your views here.
def home(request):
    data = """
        We are creating some CRUD Functionality...\nUrl pattern like this...\n1:CreateView url pattern => create/\n2:ReadView url pattern => readview\n3:UpdateView url pattern => UpdateView/<int:id>/
        """
    
    return HttpResponse(data)
def CreateView(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('Email')
        age = request.POST.get('Age')
        gender = request.POST.get('Gender')
        country = request.POST.get('Country')

        if user_information.objects.filter(name=name).exists():
            return HttpResponse('User Already Exists!!!')
        if user_information.objects.filter(email=email).exists():
            return HttpResponse('Email Already Exists!!!')
        
        user=user_information.objects.create(name=name,email=email,Age=age,gender=gender,country=country)
        user.save()
        return redirect('readview')
    
    return render(request,'CRUD/Template/create/create.html')
def ReadView(request):
    datafatch = user_information.objects.all()
    content = {
            'data':datafatch,
    }
    return render(request,'CRUD/Template/read/read.html',content)
def UpdateView(request,id):
    datafatch = user_information.objects.get(id=id)
    if request.method == 'POST': 
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        datafatch.name = name
        datafatch.email = email
        datafatch.Age = age
        datafatch.gender = gender
        datafatch.country = country
        datafatch.save()
        return redirect('readview')
    
    content = {
        'data':datafatch,
    }
    return render(request,'CRUD/Template/update/update.html',content)
def DeleteView(request,id):
    datafatch = user_information.objects.get(id=id)
    datafatch.delete()
    return redirect('readview')
    
