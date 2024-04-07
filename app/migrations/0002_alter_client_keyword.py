# Generated by Django 5.0.4 on 2024-04-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='keyword',
            field=models.CharField(blank=True, help_text='The auto-generated keyword for the client.', max_length=50, null=True, unique=True),
        ),
    ]