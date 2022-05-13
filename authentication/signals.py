
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from authentication.models import UserSession

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    print("Inside login")
    UserSession.objects.get_or_create(user=kwargs.get('user')) 


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    print("Inside logout")
    UserSession.objects.filter(user=kwargs.get('user')).delete()