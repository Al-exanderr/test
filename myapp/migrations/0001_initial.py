# Generated by Django 3.2.7 on 2021-09-19 13:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(max_length=50, unique=True, verbose_name='Oтдел')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон')),
                ('start_date', models.DateField(default=None, verbose_name='Дата начала работы')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='Дата окончания работы')),
                ('position', models.CharField(default=None, max_length=50, verbose_name='Должность')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.departments')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
                'ordering': ['surname'],
            },
        ),
    ]
