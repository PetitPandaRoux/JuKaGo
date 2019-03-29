from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PIECE_POSSIBLE = (
    ('PI','Pion'),
    ('PL','Plateau'),
    ('CA','Carte'),
    ('TO','Totem'),
    ('DE', 'Dé'),
    ('SA','Sablier'),
    ('AU','Autre')
)

class Piece(models.Model):
    type_piece = models.CharField(max_length=8,choices=PIECE_POSSIBLE,default='Autre')
    description = models.TextField()
    previsualisation = models.TextField()
    url_telechargement = models.CharField(max_length=255)

class Regle(models.Model):
    materiels = models.TextField()
    tour_de_jeu = models.TextField()
    annexes = models.TextField()


class Jeu(models.Model):
    class Meta:
        verbose_name_plural = 'jeux'
    titre = models.CharField(max_length=255)
    type_jeu = models.CharField(max_length=255)
    description = models.TextField()
    regle_id = models.ForeignKey(Regle,on_delete=models.CASCADE)
    popularite = models.PositiveSmallIntegerField()
    date_creation = models.DateField()
    version = models.PositiveSmallIntegerField()
    picture_url = models.CharField(max_length=255)
    picture_in_game_url = models.CharField(max_length = 255)

class Alter_Jeu(models.Model):
    description = models.TextField()
    regle_id = models.ForeignKey(Regle,on_delete=models.CASCADE)
    popularite = models.PositiveSmallIntegerField()
    date_creation = models.DateField()
    version = models.PositiveSmallIntegerField()
    picture_in_game_url = models.CharField(max_length = 255)
    origin = models.ForeignKey(Jeu,on_delete=models.CASCADE)


class Piece_jeu(models.Model):
    piece_id = models.ForeignKey(Piece,on_delete=models.CASCADE)
    jeu_id = models.ForeignKey(Jeu,on_delete=models.CASCADE)



ROLE_POSSIBLE = (
    ('SC','Scenariste'),
    ('GD','Game Designer'),
    ('TE','Testeur'),
    ('GR','Graphiste'),
    ('CR','Créateur'),
    ('AR','Artisan')
)


class Createur(models.Model):
    auteur_id = models.ForeignKey(User,on_delete=models.CASCADE)
    jeu_id = models.ForeignKey(Jeu,on_delete=models.CASCADE)
    role = models.CharField(max_length=15,choices=ROLE_POSSIBLE,default='Créateur')

class Commentaire(models.Model):
    jeu_id = models.ForeignKey(Jeu,on_delete=models.SET('Commentaire effacé'))
    commentaire = models.TextField()
    auteur = models.ForeignKey(Createur,on_delete=models.SET('Commentaire effacé'))

