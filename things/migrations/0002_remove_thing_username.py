# Generated by Django 4.1.4 on 2022-12-09 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("things", "0001_initial")]

    operations = [migrations.RemoveField(model_name="thing", name="username")]
