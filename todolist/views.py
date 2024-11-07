from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def todolist(request):
    context = {
        'welcome_text':"Hello",
        
    }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
        'contact_text':"welcome contact page",
        
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':"Welcome about page",
        
    }
    return render(request, 'about.html', context)


