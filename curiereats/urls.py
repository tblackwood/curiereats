from os import name
from django.conf import urls
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
#from django.urls.conf import include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/', views.sign_up),

    path('customer/', include(('core.customer.urls', 'customer'))),
    path('courier/', include(('core.courier.urls', 'courier'))),  
]
