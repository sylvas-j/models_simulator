# Generated by Django 4.2.1 on 2023-06-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCourtCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, null=True)),
                ('excel_file', models.FileField(null=True, upload_to='data_files')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
