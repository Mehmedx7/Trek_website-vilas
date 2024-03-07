# Generated by Django 5.0.1 on 2024-03-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_packages_sub_heading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_to_action',
            name='heading',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='call_to_action',
            name='sub_heading',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='footer',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='header',
            name='sub_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='header',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='packages',
            name='city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='packages',
            name='days_nights',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='packages',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='packages',
            name='heading',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='packages',
            name='pax',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='packages',
            name='review_count',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='popular_destination',
            name='city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='popular_destination',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='popular_destination',
            name='heading',
            field=models.CharField(max_length=500),
        ),
    ]
