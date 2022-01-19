# Generated by Django 3.2.9 on 2022-01-19 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_auto_20220118_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalservices',
            name='caution',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ceremonyplace',
            name='caution',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='invitations',
            name='caution',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='music',
            name='caution',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='caution',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='weddinghall',
            name='caution',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
