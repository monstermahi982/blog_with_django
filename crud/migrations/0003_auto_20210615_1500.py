# Generated by Django 3.1.6 on 2021-06-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_blog_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('blog_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
