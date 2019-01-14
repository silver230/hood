from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import *
 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import *
from django.contrib import messages
 
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View

# Create your views here.
def hood(request):
    current_user= request.user
    neighbour=Neighbourhood.objects.filter()
    business =Business.objects.filter(user=request.user.id)


    return render(request, 'index.html',{"neighbour":neighbour,"current_user":current_user,"business":business})

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

# def show(request, neighbourhood_id):
#     neighbour=Neighbourhood.objects.get(pk = neighbourhood_id)
#     current_user= request.user
#     business=BusinessForm()
#     biz =Business.objects.filter(neighbourhood=neighbourhood_id)
#     context = 
#     return render(request, 'show.html', context )

def show(request,neighbourhood_id):
    try:
        neighbour=Neighbourhood.objects.get(pk = neighbourhood_id)
        current_user= request.user
        business=BusinessForm()
        biz =Business.objects.filter(neighbourhood=neighbourhood_id)
    except Business.DoesNotExist:
        raise Http404()
    return render(request, 'show.html', {"neighbour":neighbour,"current_user":current_user,"business":business,"biz":biz}) 

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
        return redirect('show')

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


# @login_required(login_url='/login')
def profile(request):
    profile =Profile.objects.filter(user=request.user.id)
    neighbour =Neighbourhood.objects.filter(user=request.user.id)
    # commented = CommentForm()
    return render(request, 'profile.html', {"profile": profile, "neighbour": neighbour})

# @login_required( login_url='/login' )
def edit(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'edit.html' , {"form": form} )

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have editted your profile' ))
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form }
    return render(request, 'edit_profile.html',context)

# @login_required(login_url='/login')
def dump(request,pk):
    profile =Profile.objects.filter(user=request.user.id)
    neighbour =Neighbourhood.objects.filter(user=request.user.id)
    # commented = CommentForm()
    return render(request,'dump.html',{"profile": profile, "neighbour": neighbour})

# @login_required( login_url='/login' )
def create(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.neighbourhood=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'create.html' , {"form": form} )





def search(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbor = Neighbourhood.search_by_name(search_term)
        # message=f'{search_term}'
        return render(request, 'search.html',{"neighbour": searched_neighbor})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



class AlbumUpdate(UpdateView):
   model=Neighbourhood
   template_name = 'edit-neighbour.html'
   fields = ['neighbourhood_name','neighbourhood_location','area','occupants_count']

class ProfileUpdate(UpdateView):
   model= Profile
   template_name = 'edit.html'
   fields = ['contact','bio','picture']


class AlbumDelete(DeleteView):
   model=Neighbourhood
   success_url = reverse_lazy('profile')

class ProfileDelete(DeleteView):
   model=Profile
   success_url = reverse_lazy('profile')


