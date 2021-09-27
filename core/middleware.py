from django.contrib.auth.models import User
from .models import Customer, Courier

class ProfileMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        
        
        if("customer" in request.path):
            if request.user.is_authenticated and not hasattr(request.user, 'customer'):
                if not hasattr(request.user, 'courier'):
                    print("Fuck")
                    Customer.objects.create(user=request.user)
        
        if("courier" in request.path):
            if request.user.is_authenticated and not hasattr(request.user, 'courier'):
                if not hasattr(request.user, 'customer'):
                    print('Fuck yeh')
                    Courier.objects.create(user=request.user)

        response = self.get_response(request)

        
        return response