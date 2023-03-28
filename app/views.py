from django.shortcuts import render

# Create your views here.
def boot(request):
    return render(request,'new.html')