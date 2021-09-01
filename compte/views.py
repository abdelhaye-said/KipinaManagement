from django.shortcuts import redirect, render
from .models import *
from .forms import*
from django.views.generic import TemplateView
import pandas as pd
from .utils import*

# Create your views here.
def accueil(request): 
    return render(request,'compte/base.html')

def dashboard(request): 
    enf=Enfant.objects.all()
    total4J=enf.filter(claSSe='Foxes').count()
    total6J=enf.filter(claSSe='Little-Foxes').count()
    total5J=enf.filter(claSSe='Bears').count()
    total7J=enf.filter(claSSe='Seals').count()
    total8J=enf.filter(claSSe='Owls').count()
    total=enf.count()

    context={
        'enf':enf,
        'total': total,
        'total4J':total4J,
        'total6J':total6J,
        'total5J':total5J,
        'total7J':total7J,
        'total8J':total8J,
    }
    return render(request,'compte/dashboard.html',context)

def cantine(request): 
    enf=Cantine.objects.all()
    total4J=enf.filter(type_cantine='4j').count()
    total5J=enf.filter(type_cantine='5j').count()
    context={
        'enf':enf,
        'total4J' : total4J,
        'total5J' : total5J,
    }
    return render(request,'compte/cantine.html', context)

def assurance(request): 
    enf=Assurance.objects.all()
    ASSURE=enf.filter(assure='OUI').count()
    NON_ASSURE=enf.filter(assure='NON').count()
    context={
        'enf':enf,
        'ASSURE' : ASSURE,
        'NON_ASSURE' : NON_ASSURE,
    }
    return render(request,'compte/assurance.html', context)

def garde(request): 
    enf=Service_Garde.objects.all()
    total1=enf.filter(type_garde='AM').count()
    total2=enf.filter(type_garde='PM').count()
    total3=enf.filter(type_garde='AM-PM').count()
    total4=enf.filter(type_garde='Mercredi PM').count()
    total5=enf.filter(type_garde='NON').count()

    context={
        'enf':enf,
        'total1' : total1,
        'total2' : total2,
        'total3' : total3,
        'total4' : total4,
        'total5' : total5,
    }
    return render(request,'compte/garde.html', context)

def search(request):
    if request.method == "POST":
        searched= request.POST['searched']

        enf=Enfant.objects.filter(name__contains=searched)
        context={
            'searched':searched,
            'enf':enf,
        }

        return render(request,'compte/search.html',context)

    else:

        return render(request,'compte/search.html')

def forfait(request): 
    enf=Forfait.objects.all()
    total4J=enf.filter(type_forfait='journee-complte').count()
    total5J=enf.filter(type_forfait='demi-journee-matinee').count()
    total_2=enf.filter(type_forfait='demi-journee-apres-midi').count()
    total_3=enf.filter(type_forfait='2-jours-par-semaine').count()
    context={
        'enf':enf,
        'total4J' : total4J,
        'total5J' : total5J,
        'total_2':total_2,
        'total_3':total_3,
    }
    return render(request,'compte/forfait.html', context)

def Create_profil(request):
    form=create_profil()
    if request.method=="POST" :
        form=create_profil(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Create_other')

    context={
        'form': form,
    }
    return render(request,'compte/create_profit.html',context)

def update_profil(request,pk):
    enf=Enfant.objects.get(id=pk)
    form=create_profil(instance=enf)

    if request.method=="POST" :
        form=create_profil(request.POST,instance=enf)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form': form,
    }
    return render(request,'compte/update_profit.html',context)

def remove_profil(request,pk):
    enf=Enfant.objects.get(id=pk)
    if request.method=="POST" :
        enf.delete()
        return redirect('/')
    context={
        'enf': enf,
    }
    return render(request,'compte/remove_pro.html',context)

def remove_cantine(request,pk):
    enf=Cantine.objects.get(id=pk)
    if request.method=="POST" :
        enf.delete()
        return redirect('/')
    context={
        'enf': enf,
    }
    return render(request,'compte/remove_cantine.html',context)


def view_profil(request,pk): 
    enf=Enfant.objects.get(id=pk)
    context={
        'pk':pk,
        'enf':enf,
    }

    return render(request,'compte/view_profil.html',context)

def suivi_profil(request,pk):
    enf=Enfant.objects.get(id=pk)
    if request.method=="POST" :
        enf.delete()
        return redirect('/')
    context={
        'enf': enf,
    }
    return render(request,'compte/suivi.html',context)

def suivi_forfait(request):

    return render(request,'compte/suiviforfait.html')
def suivi_cantine(request):
 
    return render(request,'compte/suivicantine.html')

def suivi_transport(request):
 
    return render(request,'compte/suivitransport.html')
def suivi_garde(request):
 
    return render(request,'compte/suivigarde.html')
def suivi_assur(request):
 
    return render(request,'compte/suiviassurance.html')

def create_other(request):
    form1=create_cantine()
    form2=create_forfait()
    form3=create_assurance()
    form6=create_transport()
    form7=create_garde()
    if request.method=="POST" :
        form1=create_cantine(request.POST)
        form2=create_forfait(request.POST)
        form3=create_assurance(request.POST)
        form6=create_garde(request.POST)
        form7=create_transport(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and  form6.is_valid() and form7.is_valid()  :
            form1.save()
            form2.save()
            form3.save()
            form6.save()
            form7.save()
            return redirect('/')

    context={
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form6': form6,
        'form7': form7,
    }
    return render(request,'compte/create_other.html',context)

