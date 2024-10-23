from django.shortcuts import redirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView

def custom_google_login(request):
    adapter = GoogleOAuth2Adapter(request)
    
    return redirect(adapter.authorize_url)