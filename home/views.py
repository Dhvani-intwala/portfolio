from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def contact(request):
    """
    View to return the index page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect('/home/index?submitted=True')

        else:
            form = ContactForm()
            messages.warning(request, 'Message not sent. Please try again.')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()
 
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'home/index.html',context)
