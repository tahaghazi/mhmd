from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def home(request):
    profile = get_object_or_404(Profile)
    full_name =str( profile.first_name +' '+ profile.last_name).upper()

    return render(request,'home.html',context={'title':full_name,'profile':profile})
def about(request):
    profile = get_object_or_404(Profile)
    full_name =str( profile.first_name +' '+ profile.last_name).upper()

    return render(request,'about.html',context={'title':'about','profile':profile})
def portfolio(request):
    proj = Portfolio.objects.all()
    return render(request,'portfolio.html',context={'title':'portfolio','proj':proj})
def contact(request):
    profile = get_object_or_404(Profile)
    if request.method == 'POST':
        comment_form = ContactForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            comment_form = ContactForm()
    else:
        comment_form = ContactForm()
    return render(request,'contact.html',context={'title':'contact','profile':profile,'form':comment_form})


