from django.shortcuts import render
from authentication.models import user_default, Author
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse



class LoginView (View):
    http_method_names = [u'get', u'post']

    def get(self,request):
        return render(request,'index.html')

class TesteView (View):
    http_method_names = [u'get', u'post']

    def get(self,request):
        return render(request,'teste.html')

class AuthorCreate(CreateView):
    model = Author
    template_name = "create.html"
    fields = ['name']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')

class AuthorDetailView(DetailView):

    model = Author
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView,
                        self).get_context_data(**kwargs)
        context['name'] = Author.objects.all()
        return context
