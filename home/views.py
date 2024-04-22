from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
# from django.http import HttpResponseRedirect
from django.contrib import messages
# from home.models import ContactMessage

# Create your views here.
def send_confirmation_email(contact_email):
    """Send the user a confirmation email"""
    subject = render_to_string(
        'home/thankyou_emails/thankyou_email_subject.txt',
    )
    # Remove line breaks from the subject
    subject = ''.join(subject.splitlines())

    body = render_to_string(
        'home/thankyou_emails/thankyou_email_body.txt',
        {'contact_email': contact_email}
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [contact_email]
    )

def send_notification_email(name, email, message):
    """Send notification email to admin"""
    subject = 'New Contact Form Submission'
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

def contact(request):
    """
    View to return the index page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()
            send_confirmation_email(contact_instance.email)
            send_notification_email(contact_instance.name, contact_instance.email, contact_instance.message)
            messages.success(request, 'Your message has been sent!')

            # return HttpResponseRedirect('/#contact/?submitted=True')
              # Get the current scroll position
            scroll_position = request.POST.get('scroll_position', '0')
            # Redirect to the same page with the scroll position as a query parameter
            return redirect('/', scroll_position=scroll_position)
        else:
            messages.warning(request, 'Message not sent. Please try again.')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()
 
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)
