# Generated by Django 5.0.4 on 2024-04-08 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_chinesestorage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UzbekStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(help_text='The date and time when the product was created.')),
                ('price', models.DecimalField(decimal_places=2, help_text='The price of the product.', max_digits=20)),
                ('status', models.BooleanField(default=False, help_text='The status of the product.')),
                ('chinese_storage', models.ForeignKey(help_text='The Trek code of the product.', on_delete=django.db.models.deletion.CASCADE, related_name='uzbek_storages', to='app.chinesestorage')),
                ('client', models.ForeignKey(help_text='The keyword of the client.', on_delete=django.db.models.deletion.CASCADE, related_name='uzbek_storages', to='app.client')),
                ('party', models.ForeignKey(help_text='The title of the party.', on_delete=django.db.models.deletion.CASCADE, related_name='uzbek_storages', to='app.party')),
            ],
        ),
    ]
