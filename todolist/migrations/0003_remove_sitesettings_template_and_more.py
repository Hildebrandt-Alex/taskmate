# Generated by Django 5.1.2 on 2024-10-31 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_sitesettings_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='template',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='current_template',
            field=models.CharField(choices=[('base1.html', 'navbar 1'), ('base2.html', 'navbar 2'), ('base3.html', 'navbar 3')], default='template1', max_length=50),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='description',
            field=models.TextField(blank=True, help_text='Description of the selected template'),
        ),
    ]
