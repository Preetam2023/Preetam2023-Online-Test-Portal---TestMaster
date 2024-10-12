# Generated by Django 5.1.2 on 2024-10-12 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('options', models.JSONField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('difficulty', models.CharField(max_length=20)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.subject')),
            ],
        ),
    ]