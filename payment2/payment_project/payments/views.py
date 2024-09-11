import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_form(request):
    context = {'stripe_pub_key': settings.STRIPE_PUBLISHABLE_KEY}
    return render(request, 'payments/payment_form.html', context)

def charge(request):
    if request.method == 'POST':
        # Get the token from the form
        token = request.POST.get('stripeToken')

        try:
            # Create a charge
            charge = stripe.Charge.create(
                amount=5000,  # $50.00 this is in cents
                currency='usd',
                description='Example charge',
                source=token,
            )
            return JsonResponse({'status': 'success', 'message': 'Payment successful!'})
        except stripe.error.StripeError as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return redirect('payment_form')
