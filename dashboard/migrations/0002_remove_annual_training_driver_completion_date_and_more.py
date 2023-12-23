# Generated by Django 4.2.6 on 2023-10-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="completion_date",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="training",
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train10_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN10 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train11_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN11 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train12_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN12 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train1_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN1 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train2_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN2 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train3_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN3 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train4_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN4 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train5_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN5 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train6_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN6 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train7_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN7 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train8_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN8 Completed"),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train9_completed",
            field=models.BooleanField(default=False, verbose_name="TRAIN9 Completed"),
        ),
    ]
