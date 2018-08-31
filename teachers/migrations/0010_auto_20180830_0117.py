# Generated by Django 2.1 on 2018-08-29 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_auto_20180830_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('high_points', models.PositiveIntegerField(unique=True)),
                ('low_points', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Points',
            },
        ),
        migrations.RemoveField(
            model_name='points',
            name='grade',
        ),
        migrations.AddField(
            model_name='grades',
            name='points',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Points',
        ),
    ]
