# Generated by Django 4.1.7 on 2023-06-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadownload', '0010_alter_plotfile_plot_avr_surv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotfile',
            name='plot_hazard12m',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='plotfile',
            name='plot_hazard3m',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='plotfile',
            name='plot_hazard6m',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
