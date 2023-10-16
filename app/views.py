from django.shortcuts import render

# Create your views here.
def jspider(request):
    return render(request,'jspider.html')

def qspider(request):
    return render(request,'qspider.html')