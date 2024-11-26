from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import contact




# Create your views here.
#def home(request):
 #   return render(request,'home.html')
def contact(request):
    if request.method=="POST":
       print('post')
       name=request.POST.get('name')
       email=request.POST.get('email')
       contact=request.POST.get('contact')
       number=request.POST.get('number')
       print(name,email,number,contact)

       if len(name)>1 and len(name)<30:
           pass
       else:
           messages.error(request,'length of name should be greater than 2 and less than 30 words')
           return render(request,'home.html')
       
       if len(email)>1 and len(email)<30:
           pass
       else:
           messages.error(request,'invalid email try again')
           return render(request,'home.html')
       
       if len(number)>2 and len(number)<13:
           pass
       else:
           messages.erroe(request,'invalid number try again')
           return render(request,'home.hmtl')
       ins=models.Contact(name=name,email=email,contact=contact,number=number)
       ins.save()
       messages.success(request,'Thank You for contacting me || ypur eassage as been saved')
       print('data has been saved to database')
       print('the reqyuest is no pass')

    return render(request,'home.html')   