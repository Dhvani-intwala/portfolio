from django.shortcuts import render, reverse, redirect
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
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            # return HttpResponseRedirect('/#contact/?submitted=True')
              # Get the current scroll position
            scroll_position = request.POST.get('scroll_position', '0')
            print(scroll_position)
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
