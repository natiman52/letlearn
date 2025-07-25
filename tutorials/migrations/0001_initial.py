# Generated by Django 4.2 on 2025-07-13 21:21

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('video', models.URLField(blank=True, max_length=500, null=True)),
                ('conclusion', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('identifier', models.CharField(max_length=200, null=True)),
                ('slug', models.CharField(blank=True, max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('courseName', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('identifier', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vedios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(default='Blank', max_length=250)),
                ('video', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitAndTutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('Tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.tutorial')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.unit')),
            ],
        ),
        migrations.CreateModel(
            name='UnitAndChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('Chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.chapter')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.unit')),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='chapters',
            field=models.ManyToManyField(blank=True, through='tutorials.UnitAndChapter', to='tutorials.chapter'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='units',
            field=models.ManyToManyField(blank=True, through='tutorials.UnitAndTutorial', to='tutorials.unit'),
        ),
        migrations.CreateModel(
            name='collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to='images')),
                ('desc', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('courses', models.ManyToManyField(to='tutorials.tutorial')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='additional_video',
            field=models.ManyToManyField(blank=True, null=True, to='tutorials.vedios'),
        ),
    ]
