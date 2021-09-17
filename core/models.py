from django.db import models

class Depoimentos(models.Model):
    nome_cargo=models.CharField('Nome+Cargo',max_length=150)
    foto=models.ImageField(upload_to='fotos')
    depoimento=models.CharField('Depoimento',max_length=250)

class Redes_Sociais(models.Model):
    facebook=models.CharField('Facebook',max_length=100)
    twitter=models.CharField('Twitter', max_length=100)
    pinterest=models.CharField('Pinterest', max_length=100)
    instagram=models.CharField('Instagram', max_length=100)
    youtube=models.CharField('Youtube', max_length=100)

class Downloads(models.Model):
    apple_store=models.CharField('Link Apple Store',max_length=100)
    google_play=models.CharField('Link Google Play',max_length=100)