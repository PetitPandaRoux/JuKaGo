# Generated by Django 2.1.7 on 2019-03-29 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jeux', '0002_auto_20190329_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alter_jeu',
            old_name='regle_id',
            new_name='regle',
        ),
        migrations.RenameField(
            model_name='commentaire',
            old_name='jeu_id',
            new_name='jeu',
        ),
        migrations.RenameField(
            model_name='createur',
            old_name='auteur_id',
            new_name='auteur',
        ),
        migrations.RenameField(
            model_name='createur',
            old_name='jeu_id',
            new_name='jeu',
        ),
        migrations.RenameField(
            model_name='jeu',
            old_name='regle_id',
            new_name='regle',
        ),
        migrations.RenameField(
            model_name='piece_jeu',
            old_name='jeu_id',
            new_name='jeu',
        ),
        migrations.RenameField(
            model_name='piece_jeu',
            old_name='piece_id',
            new_name='piece',
        ),
        migrations.AddField(
            model_name='jeu',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
