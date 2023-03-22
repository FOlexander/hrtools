# Generated by Django 4.1.7 on 2023-03-22 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datadownload', '0006_auto_20230307_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotfile',
            name='plot',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.CreateModel(
            name='ControlPlotFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.ImageField(null=True, upload_to='uploads/')),
                ('plot_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]