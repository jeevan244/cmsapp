# Generated by Django 4.0.4 on 2022-07-01 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty')], max_length=7)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(max_length=6)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='authenticate.customuser')),
            ],
        ),
    ]
