# Generated by Django 4.0.6 on 2022-07-25 10:01

from django.db import migrations, models
import django.db.models.deletion
import todo_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=todo_app.models.one_week_hence)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.todolist')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
