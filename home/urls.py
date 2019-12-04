from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, LoansPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('loans.html', LoansPageView.as_view(), name='loans'),
    path('contact.html', ContactPageView.as_view(), name='contact'),
    path('index.html', HomePageView.as_view(), name='index'),
    path('about-us.html', AboutPageView.as_view(), name='about'),
]
