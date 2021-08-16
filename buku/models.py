import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Penerbit(models.Model):
    nama = models.CharField(max_length=100)
    website = models.URLField(null=True,blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nama

class Kategori(models.Model):
    nama = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=200)
    kategori = models.ForeignKey(Kategori,on_delete=models.CASCADE)
    penulis = models.CharField(max_length=50)
    tahun = models.PositiveIntegerField(default=current_year(),
            validators=[MinValueValidator(1900), max_value_current_year])
    penerbit = models.ForeignKey(Penerbit,on_delete=models.CASCADE)
    sampul = models.ImageField(null=True,blank=True,upload_to="sampul/")

    def __str__(self):
        return self.judul








