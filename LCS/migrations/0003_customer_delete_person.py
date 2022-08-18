# Generated by Django 4.0.6 on 2022-08-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LCS', '0002_supplier_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=70)),
                ('mobile', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='person',
        ),
    ]