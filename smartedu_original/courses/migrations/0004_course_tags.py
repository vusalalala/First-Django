# Generated by Django 3.1.7 on 2021-03-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Tag'),
        ),
    ]
