from django.shortcuts import render


def index(request):
    return render( request , "uffs/index.html", {"name": "Alex"                  
    })
def pepe(request, name):
    return render( request , "uffs/index.html", {"name": name.capitalize()                  
    })