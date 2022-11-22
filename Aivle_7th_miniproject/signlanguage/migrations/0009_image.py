# Generated by Django 3.2 on 2022-11-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0008_aimodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('answer', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]