# Generated by Django 3.1.6 on 2021-06-15 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('section', models.SlugField()),
                ('age', models.IntegerField()),
                ('tupc_id', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gclassroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('task', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('file', models.FileField(blank=True, default='none', upload_to='')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreateTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasknumber', models.SlugField()),
                ('announcement', models.TextField()),
                ('startdate', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('upload_file', models.FileField(blank=True, default='none', upload_to='')),
                ('teacher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreateQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField()),
                ('Q1', models.TextField(blank=True, default='')),
                ('a1', models.CharField(blank=True, default='', max_length=50)),
                ('b1', models.CharField(blank=True, default='', max_length=50)),
                ('c1', models.CharField(blank=True, default='', max_length=50)),
                ('d1', models.CharField(blank=True, default='', max_length=50)),
                ('Q2', models.TextField(blank=True, default='')),
                ('a2', models.CharField(blank=True, default='', max_length=50)),
                ('b2', models.CharField(blank=True, default='', max_length=50)),
                ('c2', models.CharField(blank=True, default='', max_length=50)),
                ('d2', models.CharField(blank=True, default='', max_length=50)),
                ('Q3', models.TextField(blank=True, default='')),
                ('a3', models.CharField(blank=True, default='', max_length=50)),
                ('b3', models.CharField(blank=True, default='', max_length=50)),
                ('c3', models.CharField(blank=True, default='', max_length=50)),
                ('d3', models.CharField(blank=True, default='', max_length=50)),
                ('Q4', models.TextField(blank=True, default='')),
                ('a4', models.CharField(blank=True, default='', max_length=50)),
                ('b4', models.CharField(blank=True, default='', max_length=50)),
                ('c4', models.CharField(blank=True, default='', max_length=50)),
                ('d4', models.CharField(blank=True, default='', max_length=50)),
                ('teacher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=50, null=True)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('in_and_out', models.CharField(choices=[('Check-In', 'Check-In'), ('Check-Out', 'Check-Out')], max_length=50, null=True)),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=50, null=True)),
                ('answer2', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=50, null=True)),
                ('answer3', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=50, null=True)),
                ('answer4', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=50, null=True)),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
