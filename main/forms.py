from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length = 100, required =True, 
            widget = forms.TextInput(attrs= {
                'class':'form-input',
                'type':'text',
                'name':'fullname',
                'placeholder':'* Full name...',
            }))
    email = forms.EmailField(max_length=254, required=True, 
            widget = forms.TextInput(attrs = {
                'class':'form-input',
                'name':'email',
                'type': 'email',
                'placeholder':'*Email..',
            }))
    message = forms.CharField(max_length = 254, required=True,
            widget = forms.Textarea(attrs={
                'class':'form-input',
                'name':'message',
                'placeholder': '*Message..',
                'rows' : 6,
            }))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message')
