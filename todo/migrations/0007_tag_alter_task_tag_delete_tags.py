# Generated by Django 5.0.3 on 2024-04-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_rename_tags_task_tag_tags_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(to='todo.tag'),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]