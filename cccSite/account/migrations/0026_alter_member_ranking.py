# Generated by Django 4.2.6 on 2024-03-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_alter_member_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='ranking',
            field=models.SmallIntegerField(choices=[(1, 'member'), (2, 'trusted member'), (99, 'admin'), (98, 'moderator'), (-1, 'banned')], default=1),
        ),
    ]