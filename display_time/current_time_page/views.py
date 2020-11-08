from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def index(request):
    print("hello, this page is requesting...please wait.")
    return render(request,"index.html")

def current_time(request):
    context = {
        "time": strftime("%A %B %d, %Y %H:%M %p", gmtime())
    }
    return render(request,'current_time.html', context)
