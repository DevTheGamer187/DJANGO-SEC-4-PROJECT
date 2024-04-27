from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def receipe(request):


    if request.method=="POST":
        data=request.POST
        file=request.FILES

        receipename=data.get('receipename')
        receipedesc=data.get('receipedesc')
        receipeimg=file.get('receipeimg')
        print(receipename)
        print(receipedesc)
        print(receipeimg)    

        Receipebook.objects.create(
            receipename=receipename,
            receipedesc=receipedesc,
            receipeimg=receipeimg,
        )
        return redirect('/')
    queryset=Receipebook.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(receipename__icontains=request.GET.get('search'))

    context={'receipe':queryset}
        

    return render(request,"index.html",context)
def receipedata(request):
    queryset=Receipebook.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(receipename__icontains=request.GET.get('search'))

    context={'receipe':queryset}
        

    return render(request,"data.html",context)

def delete_receipe(request,id):
    item=Receipebook.objects.all().get(id=id)
    item.delete()
    return redirect('/')
def update_receipe(request,id):
    queryset=Receipebook.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        file=request.FILES

        receipename=data.get('receipename')
        receipedesc=data.get('receipedesc')
        receipeimg=file.get('receipeimg')

        queryset.receipename=receipename
        queryset.receipedesc=receipedesc
        
        if receipeimg:
            queryset.receipeimg=receipeimg
            
        queryset.save()
        return redirect("/")
    context={'receipe':queryset}

    return render(request,"update-receipe.html",context)