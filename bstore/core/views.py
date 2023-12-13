from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

    context = {}
    
    return render(request, 'core/index.html', context)

def floor(request):

    context = {}
    
    return render(request, 'core/floor.html', context)

def design(request):

    context = {}
    
    return render(request, 'core/design.html', context)


def pop(request):

    context = {}
    
    return render(request, 'core/pop.html', context)


def interior(request):

    context = {}
    
    return render(request, 'core/interior.html', context)

def real(request):

    context = {}
    
    return render(request, 'core/real.html', context)

def contact(request):

    context = {}
    
    return render(request, 'core/contact.html', context)