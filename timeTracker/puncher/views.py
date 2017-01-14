from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'dummy': " - go! - "}
    return render(request, 'puncher/index.html', context)
