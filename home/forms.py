from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Contact Us form
    """
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'message',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = False
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-3 '
                                                        'contact-form-input')
            self.fields[field].label = False