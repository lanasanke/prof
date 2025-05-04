from django.shortcuts import render

# Create your views here.

def pengguna(request):
    return render(request,'pengguna/pengguna.html')