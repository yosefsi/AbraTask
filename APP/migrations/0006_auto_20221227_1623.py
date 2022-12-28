# Generated by Django 3.2.16 on 2022-12-27 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP', '0005_alter_massage_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sender',
            name='user',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='sender',
        ),
        migrations.AddField(
            model_name='massage',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='massage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='massage',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='massage',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='RECEIVER',
        ),
        migrations.DeleteModel(
            name='SENDER',
        ),
    ]
