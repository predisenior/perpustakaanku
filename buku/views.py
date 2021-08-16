from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import Buku


# class BukuView(TemplateView):
#     model = Buku
#     # context_object_name = 'list_buku' 
#     template_name = 'home.html'

class UjicobaView(TemplateView):
    template_name = 'uji.html'

class BukuCreateView(CreateView):
    model = Buku
    template_name = 'inputbuku.html'
    fields = ['judul','penulis','kategori','tahun','penerbit','sampul']

class BukuListView(LoginRequiredMixin,ListView):
    model = Buku
    template_name = 'home.html'
    login_url = 'login'
