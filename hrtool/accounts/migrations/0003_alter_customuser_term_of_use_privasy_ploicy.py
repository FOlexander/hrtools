# Generated by Django 4.1.7 on 2023-06-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_term_of_use_privasy_ploicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='term_of_use_privasy_ploicy',
            field=models.BooleanField(blank=True),
        ),
    ]
