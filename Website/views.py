from django.shortcuts import render
from Website.forms import ContactForm,NewsletterForm
from django.http import HttpResponseRedirect
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = 'unknown'
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket did not submited successfully')
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your Email submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your Email did not submited successfully')
        return HttpResponseRedirect('/') 
    else:
        return HttpResponseRedirect('/') 
    
    
def maintenance(request):
    return render(request, 'maintenance.html')