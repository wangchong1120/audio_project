# Generated by Django 2.0.6 on 2019-08-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QTFMUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(max_length=20, unique=True)),
                ('u_telephone', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'qtfm_user',
            },
        ),
    ]
