# Generated by Django 4.1.7 on 2023-06-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadownload', '0008_plotfile_plot_hazard12m_plotfile_plot_hazard3m_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotfile',
            name='plot_avr_surv',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
            preserve_default=False,
        ),
    ]
