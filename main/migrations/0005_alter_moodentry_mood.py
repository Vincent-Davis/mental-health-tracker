# Generated by Django 5.1.1 on 2024-10-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_moodentry_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodentry',
            name='mood',
            field=models.CharField(max_length=255),
        ),
    ]
