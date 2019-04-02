from django.contrib import admin
from jeux.models import Jeu,Regle,Piece,Createur

# Register your models here.

admin.site.register(Jeu)
admin.site.register(Regle)
admin.site.register(Piece)
admin.site.register(Createur)