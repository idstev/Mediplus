from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# Create your views here.
def contact(request):
    #print("tipo de peticion: ", request.method)
    #instaciar la clase
    contactForm=ContactForm()
    if request.method == "POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            emailContacto=EmailMessage(
                "MediPlus SA: Nuevo mensaje de contacto",
                "De {} <{}>\n\nMensaje:\n\n{}".format(name,email,message),
                "cliente@gmail.com",
                ["mediplus@imbox.mailtrap.io"],
                reply_to=[email]
            )
            try:
                emailContacto.send()
                return redirect(reverse('contact')+"?success")
            except Exception as e:
                print("error",type(e).__name__)
                return redirect(reverse('contact')+"?fail")


    return render(request, "contact/contact.html", {'contactForm':contactForm})