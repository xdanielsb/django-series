from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from apps.pet.forms import PetForm
from apps.pet.models import Pet

def index(request):
    return render(request, 'pet/index.html')

def pet_view(request):
    if request.method == 'POST':
        form  = PetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pets-index')
    else:
        form = PetForm()
    return render(request , 'pet/pet_form.html', {'form':form})


def pet_list(request):
    pets = Pet.objects.all()
    ctx = {'pets':pets}
    return render(request, 'pet/pet_list.html', ctx)
