from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import *

# Create your views here.
def hood(request):
    current_user= request.user
    neighbour=Neighbourhood.objects.all()
    

    return render(request, 'index.html')

def new_neighbour(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbour = form.save(commit=False)
            neighbour.user = current_user
            neighbour.save()
        return redirect('hood')

    else:
        form = NeighbourhoodForm()
    return render(request,'hood.html', {"form": form})  


