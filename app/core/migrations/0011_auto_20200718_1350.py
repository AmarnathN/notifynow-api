# Generated by Django 3.0.7 on 2020-07-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200718_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermail',
            name='mail_from',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='consent',
            unique_together={('user', 'notification_type')},
        ),
    ]
