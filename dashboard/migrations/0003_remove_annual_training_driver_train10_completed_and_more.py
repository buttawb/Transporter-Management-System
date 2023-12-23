# Generated by Django 4.2.6 on 2023-10-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_remove_annual_training_driver_completion_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train10_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train11_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train12_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train1_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train2_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train3_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train4_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train5_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train6_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train7_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train8_completed",
        ),
        migrations.RemoveField(
            model_name="annual_training_driver",
            name="train9_completed",
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train10_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN10 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train11_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN11 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train12_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN12 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train1_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN1 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train2_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN2 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train3_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN3 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train4_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN4 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train5_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN5 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train6_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN6 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train7_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN7 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train8_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN8 Completed Date"
            ),
        ),
        migrations.AddField(
            model_name="annual_training_driver",
            name="train9_completed_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="TRAIN9 Completed Date"
            ),
        ),
    ]
