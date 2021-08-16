from django.contrib import admin
from .models import Penerbit, Kategori, Buku


class BukuAdmin(admin.ModelAdmin):
    model = Buku
    ordering = ['judul']
    list_display = ('judul', 'penulis', 'penerbit','tahun')
    search_fields = ['judul', 'penulis']


admin.site.register(Kategori)
admin.site.register(Penerbit)
admin.site.register(Buku, BukuAdmin)
