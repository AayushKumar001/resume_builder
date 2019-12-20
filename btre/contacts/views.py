from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        print('******Listing Name:'+listing)
        #check if the user has already made enquiry

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an enquiry to this listing')
                return redirect('/listings/list/'+listing_id)
    
        contact = Contact(listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        #send_mail("Property Listing Enquiry","There has been an enquiry for "+listing+".Sign into the admin info for details",'bhagwadgeeta12345@gmail.com',[realtor_email,'aayush63kumar@gmail.com'],fail_silently=False)
        send_mail("Property Listing Enquiry","There has been an enquiry for "+listing+".Sign into the admin info for details","bhagwadgeeta12345@gmail.com",[realtor_email,'aayush63kumar@gmail.com'],fail_silently=False,auth_user=None,auth_password=None)
        messages.success(request,"Your request has been submitted,a realtor will get back soon")

    
    return redirect('/listings/list/'+listing_id)
    

    
    