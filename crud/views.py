from django.shortcuts import render,HttpResponse


def menu(request):
    return render(request,"index.html",{})