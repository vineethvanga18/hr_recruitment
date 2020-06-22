# Generated by Django 3.0.7 on 2020-06-22 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Objective', models.TextField(max_length=128)),
                ('skills_required', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('skills', models.TextField(max_length=128)),
                ('Applying_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Application')),
            ],
        ),
    ]
