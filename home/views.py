from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutPageView(View):
    def get(self, request):
        return render(request, 'about-us.html')


class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact.html')


class LoansPageView(View):
    def get(self, request):
        return render(request, 'loans.html')


class ElementPageView(View):
    def get(self, request):
        return render(request, 'elements.html')


class NewsPageView(View):
    def get(self, request):
        return render(request, 'news.html')
