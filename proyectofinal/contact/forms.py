from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': 'Email_text','placeholder': 'Ingrese su nombre'}), min_length=4, max_length=10)
    email=forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class': 'Email_text','placeholder': 'Ingrese su email'}))
    message=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class': 'massage-bt','placeholder': 'Ingrese su mensaje'}), min_length=20, max_length=1000)