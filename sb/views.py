from django.shortcuts import render

# Create your views here.
def sb_home(request):
    return render(request,'sb_home.html')
