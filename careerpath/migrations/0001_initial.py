# Generated by Django 5.2.4 on 2025-07-16 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('focus', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='careerpath.field')),
                ('key_skills', models.ManyToManyField(related_name='job_examples', to='careerpath.skill')),
            ],
        ),
        migrations.CreateModel(
            name='LearningResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('job_example', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_resources', to='careerpath.jobexample')),
            ],
        ),
        migrations.CreateModel(
            name='RealWorldProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_example', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='real_world_projects', to='careerpath.jobexample')),
            ],
        ),
        migrations.CreateModel(
            name='Subfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('common_job_titles', models.JSONField(default=list)),
                ('key_tools_skills', models.JSONField(default=list)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subfields', to='careerpath.field')),
            ],
        ),
    ]
