from django.shortcuts import render, reverse, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def contact(request):
    """
    View to return the index page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(subject, message, email, ['intdhvani2627@gmail.com'])
            form.save()
            messages.success(request, 'Your message has been sent!')
            # return HttpResponseRedirect('/#contact/?submitted=True')
              # Get the current scroll position
            scroll_position = request.POST.get('scroll_position', '0')
            # Redirect to the same page with the scroll position as a query parameter
            return redirect('/', scroll_position=scroll_position)
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
