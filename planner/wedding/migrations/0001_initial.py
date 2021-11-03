# Generated by Django 3.2.9 on 2021-11-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=100)),
                ('caution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('approved', models.BooleanField()),
                ('notes', models.TextField()),
                ('importance', models.IntegerField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('spent', models.DecimalField(decimal_places=2, max_digits=8)),
                ('remaining_amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Callendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CeremonyPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=100)),
                ('caution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('approved', models.BooleanField()),
                ('notes', models.TextField()),
                ('guest_capacity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet_type', models.CharField(choices=[('S', 'Standard'), ('LF', 'Lactose Free'), ('VT', 'Vegetarian'), ('V', 'Vegan'), ('GF', 'Gluten Free'), ('F', 'Frutarian')], max_length=2)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.CharField(max_length=50)),
                ('accomodation', models.BooleanField()),
                ('age', models.IntegerField(max_length=3)),
                ('invited', models.BooleanField(default=False)),
                ('attendance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invitations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=100)),
                ('caution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('approved', models.BooleanField()),
                ('notes', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=100)),
                ('caution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('approved', models.BooleanField()),
                ('notes', models.TextField()),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=100)),
                ('caution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('approved', models.BooleanField()),
                ('notes', models.TextField()),
                ('services', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('time', models.DateField()),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WeddingHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=9)),
                ('email_address', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=100)),
                ('caution', models.DecimalField(decimal_places=2, max_digits=5)),
                ('approved', models.BooleanField()),
                ('notes', models.TextField()),
                ('accomodation', models.BooleanField()),
                ('guest_capacity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
