from django.shortcuts import render, redirect
from django.contrib import messages
from .models import alumni
from .forms import alumniForm
from django.contrib import messages



def home(request):
  data = alumni.objects.all()
  context = {'data':data}
  return render(request, 'home.html', context)
  
def about(request):
  return render(request, 'about.html',{})

def contact(request):
  return render(request, 'contact-us.html',{})

def addprofile(request):
  form = alumniForm(request.POST or None)
  data = alumni.objects.all()
  context = {"form": form,'data':data}
  if request.method == 'POST' and form.is_valid():
    form.save()
    messages.error(request, 'Alumni Data Successfully Added')
    return render(request, 'home.html', context)
  else:
    return render(request, 'addprofile.html', context)

def editprof(request,primary_key):
  data = alumni.objects.get(pk = primary_key)
  form = alumniForm(request.POST or None)
  context ={"form":form,'data':data}
  if request.method=="POST" and form.is_valid():
    data.first_name = form.cleaned_data.get('first_name')
    data.last_name = form.cleaned_data.get("last_name")
    data.gender = form.cleaned_data.get("gender")
    data.age = form.cleaned_data.get("age")
    data.save()
    messages.error(request, 'Alumni Data Successfully Edited')
    return redirect('home')
  else:
    return render(request,'editprofile.html', context)
  

def delete(request, primary_key):
  context = {"primary_key":primary_key}
  return render(request,'delete.html', context) 

def delete_now(request, primary_key):
  data = alumni.objects.get(pk = primary_key)
  data.delete()
  messages.error(request, 'Alumni Data Successfully Deleted')
  return redirect('home') 

def namesearch(request):
  if request.method=="POST":
    name = request.POST['name']
    if name == "":
      return redirect('home')
    else:
      data = alumni.objects.filter(id = name)
      context = {'data':data}
      return render(request,'namesearch.html', context)

  else:
    return redirect('home')




