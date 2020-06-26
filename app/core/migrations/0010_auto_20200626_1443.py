# Generated by Django 3.0.7 on 2020-06-26 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_userapp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consent',
            old_name='netflix_chrome_ext',
            new_name='chrome_ext',
        ),
        migrations.RenameField(
            model_name='consent',
            old_name='netflix_whatsapp',
            new_name='whatsapp',
        ),
        migrations.AddField(
            model_name='consent',
            name='app',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_app', to='core.UserApp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User'),
        ),
        migrations.AlterUniqueTogether(
            name='consent',
            unique_together={('user', 'app')},
        ),
    ]
