from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import *

# Create your views here.
def hood(request):
    current_user= request.user
    neighbour=Neighbourhood.objects.filter()
    business =Business.objects.filter(user=request.user.id)


    return render(request, 'index.html',{"neighbour":neighbour,"current_user":current_user,"bussiness":bussiness})

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

def show(request, neighbourhood_id):
    neighbour=Neighbourhood.objects.get(pk = neighbourhood_id)
    current_user= request.user
    business=BusinessForm()
    biz =Business.objects.filter(neighbourhood=neighbourhood_id)
    context = {"neighbour":neighbour,"current_user":current_user,"business":business,"biz":biz}
    return render(request, 'show.html', context )




def new_business(request, pk):
    neighbourhood = get_object_or_404(Neighbourhood,id=pk)
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            print('x')
            business.neighbourhood = neighbourhood
            business.save()
        return redirect('show', neighbourhood_id=neighbourhood.id)

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form, "neighbourhood":neighbourhood })

 

def search(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbor = Neighbourhood.search_by_name(search_term)
        # message=f'{search_term}'
        return render(request, 'search.html',{"neighbour": searched_neighbor})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
