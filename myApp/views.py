from django.shortcuts import render,redirect
from . forms import IncidentsForm,RegistrationForm
from . models import Incident
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')

def Create(request):
    if request.method == 'POST':
        form  = IncidentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncidentsForm()
    return render(request,'create.html',{'form':form})
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def Saved_Incidents(request):
    incidents = Incident.objects.all()
    return render(request,'save_incidents.html',{'incidents':incidents})