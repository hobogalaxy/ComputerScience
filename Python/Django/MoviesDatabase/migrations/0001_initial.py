# Generated by Django 2.1.3 on 2018-12-08 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('num_of_ratings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('actor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MoviesDatabase.Actor')),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MoviesDatabase.Movie')),
            ],
        ),
    ]