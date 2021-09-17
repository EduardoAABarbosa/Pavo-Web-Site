# Generated by Django 3.2.7 on 2021-09-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cargo', models.CharField(max_length=150, verbose_name='Nome+Cargo')),
                ('foto', models.ImageField(upload_to='fotos')),
                ('depoimento', models.CharField(max_length=250, verbose_name='Depoimento')),
            ],
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apple_store', models.CharField(max_length=100, verbose_name='Link Apple Store')),
                ('google_play', models.CharField(max_length=100, verbose_name='Link Google Play')),
            ],
        ),
        migrations.CreateModel(
            name='Downloads_Pacotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_29', models.CharField(max_length=100, verbose_name='Pacote 29,00')),
                ('download_39', models.CharField(max_length=100, verbose_name='Pacote 39,00')),
                ('download_49', models.CharField(max_length=100, verbose_name='Pacote 49,00')),
            ],
        ),
        migrations.CreateModel(
            name='Redes_Sociais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(max_length=100, verbose_name='Twitter')),
                ('pinterest', models.CharField(max_length=100, verbose_name='Pinterest')),
                ('instagram', models.CharField(max_length=100, verbose_name='Instagram')),
                ('youtube', models.CharField(max_length=100, verbose_name='Youtube')),
            ],
        ),
    ]