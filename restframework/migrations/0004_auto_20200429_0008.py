# Generated by Django 2.2.3 on 2020-04-29 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restframework', '0003_auto_20200428_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='relationship',
            field=models.CharField(choices=[('mum', 'Mum'), ('sister', 'Sister'), ('brother', 'Brother'), ('friend', 'Friend')], max_length=7, null=True),
        ),
    ]
