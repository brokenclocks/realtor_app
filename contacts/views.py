from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        email = request.POST['email']
        listing = request.POST['listing']
        name = request.POST['name']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        phone = request.POST['phone']

        # check if user has inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          message=message, user_id=user_id, email=email, phone=phone)

        contact.save()
# send email
# send_mail(
#     'property listing inquiry'
# )
        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/'+listing_id)
