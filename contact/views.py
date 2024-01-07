from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.


def contact(request):

    """
    a view to display the contactform
    and handle form submission
    """

    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect('/contactus?submitted=True')

        else:
            form = ContactForm()
            messages.warning(request, 'Message not sent. Please try again.')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()
 
    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)