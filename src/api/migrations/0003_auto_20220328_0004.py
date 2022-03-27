# Generated by Django 3.2.12 on 2022-03-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220327_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='predication',
            name='avg_vocal_fundamental_frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='d2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='dfa',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='hnr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='jitter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='max_vocal_fundamental_frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='min_vocal_fundamental_frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='nhr',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='ppe',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='rpde',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='shimmer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='spread1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='spread2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='predication',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='predication',
            name='audio',
            field=models.FileField(help_text='Please record voice [15sec-45sec] voice must be .wmv format', upload_to='audios/'),
        ),
    ]