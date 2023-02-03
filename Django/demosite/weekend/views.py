from django.shortcuts import render
import datetime

app_name = "weekend"

# Create your views here.
def index(request):
    n = datetime.datetime.now()
    return render(request, "weekend/index.html",{
        "weekend" : n.weekday(),
        "name" : n.strftime('%A')
    })
