# Generated by Django 4.0.2 on 2022-02-06 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apihandler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='createdat',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='guestcanpause',
            new_name='guest_can_pause',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='votestoskip',
            new_name='votes_to_skip',
        ),
    ]
