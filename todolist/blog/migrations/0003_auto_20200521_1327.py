# Generated by Django 3.0.6 on 2020-05-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
