# Generated by Django 4.1.4 on 2023-02-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_features_font_awesome_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='icon_color',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='', max_length=10000),
        ),
    ]
