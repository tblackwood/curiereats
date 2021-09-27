from os import name
from django.conf import urls
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from core import consumers, views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home_page"),
    
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/', views.sign_up),

    path('customer/', include(('core.customer.urls', 'customer'))),
    path('courier/', include(('core.courier.urls', 'courier'))),  

    path('firebase-messaging-sw.js', (TemplateView.as_view(template_name="firebase-messaging-sw.js", content_type="application/javascript",))),
]

websocket_urlpatterns = [
    path('ws/jobs/<job_id>/', consumers.JobConsumer.as_asgi())
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
