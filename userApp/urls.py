from django.urls import path

from userApp.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='Logout')
]
