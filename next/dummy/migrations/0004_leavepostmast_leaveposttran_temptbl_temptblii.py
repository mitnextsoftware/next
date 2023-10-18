# Generated by Django 4.2.5 on 2023-09-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0003_alter_employeeexperience_designation1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='leavepostmast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordid', models.IntegerField()),
                ('recorddate', models.DateField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='leaveposttran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordid', models.IntegerField()),
                ('empcode', models.CharField(max_length=10)),
                ('leaveqty', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='temptbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=10)),
                ('empname', models.CharField(max_length=50)),
                ('pfno', models.CharField(max_length=50)),
                ('payablepayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('specialamt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ariasamt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('epfamt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('epsamt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='temptblii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=10)),
                ('totalearningamt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]