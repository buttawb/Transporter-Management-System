# Generated by Django 4.2.6 on 2023-10-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0005_alter_annual_training_driver_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="annual_drill",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "drill_name",
                    models.CharField(max_length=255, verbose_name="Drill Name"),
                ),
                (
                    "drilling_month",
                    models.CharField(max_length=50, verbose_name="Dril Month"),
                ),
            ],
            options={
                "verbose_name": "Drill Training",
                "verbose_name_plural": "Drill Trainings",
            },
        ),
        migrations.CreateModel(
            name="annual_drill_driver",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user", models.CharField(max_length=255)),
                ("train1_completed_date", models.DateField(blank=True, null=True)),
                ("train2_completed_date", models.DateField(blank=True, null=True)),
                ("train3_completed_date", models.DateField(blank=True, null=True)),
                ("train4_completed_date", models.DateField(blank=True, null=True)),
                ("train5_completed_date", models.DateField(blank=True, null=True)),
                ("train6_completed_date", models.DateField(blank=True, null=True)),
                ("train7_completed_date", models.DateField(blank=True, null=True)),
                ("train8_completed_date", models.DateField(blank=True, null=True)),
                ("train9_completed_date", models.DateField(blank=True, null=True)),
                ("train10_completed_date", models.DateField(blank=True, null=True)),
                ("train11_completed_date", models.DateField(blank=True, null=True)),
                ("train12_completed_date", models.DateField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Dril Driver",
                "verbose_name_plural": "Drill Drivers",
            },
        ),
    ]
