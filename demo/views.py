from django.shortcuts import render,HttpResponse
from .models import Surname,Member
# Create your views here.

def family(request):
    Surnames = Surname.objects.all()
    Members = Member.objects.all()
    context={
        "Surnames" : Surnames,
        "Members" : Members
    }
    return render(request,"demo/family.html",context)

def selection(request,id):
    Surnames = Surname.objects.get(id=id)
    Members = Member.objects.filter(Surname=Surnames)
    context={
        "Surnames" : Surnames,
        "Members" : Members
    }
    return render(request,"demo/family.html",context)




