# Generated by Django 5.1.4 on 2024-12-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='work_from_home_availability',
            new_name='work_from_home',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_location',
        ),
        migrations.AddField(
            model_name='job',
            name='client_brand_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='culture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='is_recent',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='position_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='workplace_types',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_logo_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='employer_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='employment_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
