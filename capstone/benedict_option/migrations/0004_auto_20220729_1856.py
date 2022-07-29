# Generated by Django 3.2.5 on 2022-07-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benedict_option', '0003_auto_20220729_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_liturgies',
            field=models.ManyToManyField(blank=True, related_name='favorite_liturgies', to='benedict_option.Liturgy'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uploaded_liturgies',
            field=models.ManyToManyField(blank=True, related_name='uploaded_liturgies', to='benedict_option.Liturgy'),
        ),
        migrations.AlterField(
            model_name='user',
            name='viewed_liturgies',
            field=models.ManyToManyField(blank=True, related_name='viewed_liturgies', to='benedict_option.Liturgy'),
        ),
    ]
