from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from apps.pet.forms import PetForm

def index(request):
    return render(request, 'pet/index.html')

def pet_view(request):
    if request.method == 'POST':
        form  = PetForm(request.Post)
        if form.is_valid():
            form.save()
        return redirect('pets')
    else:
        form = PetForm()
    return render(request , 'pet/pet_form.html', {'form':form})
