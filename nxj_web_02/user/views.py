from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')
def a(requser):
    return render(requser,'a.html')