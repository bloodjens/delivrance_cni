import datetime
from django.db import models
from django.contrib.auth.hashers import make_password,check_password


class Verif(models.Model):
    contenu = models.CharField(max_length=6)


class Region (models.Model):
    nom = models.CharField(max_length=1000)
    code = models.CharField(max_length=100,default="")

class District (models.Model):
    nom = models.CharField(max_length=1000)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    code = models.CharField(max_length=100,default="")
    
class Arrondissement(models.Model):
    oui = "oui"
    non = "non"
    
    BOLLE = [
        (oui, "oui"),
        (non,"non"),
    ]
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100,default="")
    district = models.ForeignKey(District, on_delete=models.CASCADE,default="")
    diriger = models.CharField(max_length=20, choices=BOLLE, default=non)
    

    
    
    
class Utilisateur(models.Model):
    user = "user"
    admin = "admin"
    
    ROLE = [
        (user, "user"),
        (admin,"admin"),
    ]
    identifiant = models.CharField(max_length=100)
    email = models.EmailField()
    photo =  models.ImageField(upload_to='front/src/lib/image/profil',default="")
    tel = models.CharField(max_length=10)
    role = models.CharField(max_length=20, choices=ROLE, default=user)
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.CASCADE,)
    password = models.CharField(max_length=128)
    date_inscription = models.DateTimeField(default=datetime.datetime.now())
    
    
    
    def set_mot_de_passe(self, mot_de_passe):
        self.password = make_password(mot_de_passe)
    
    def verifier_password(self, mot_de_passe):
        verification = check_password(mot_de_passe)
        return verification



        
class Chef(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100,default="")
    email = models.EmailField()
    numCni = models.CharField(max_length=9, default="")
    tel = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='front/src/lib/image/chef',blank=True)
    arrondissementChef = models.ForeignKey(Arrondissement, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)
    def set_mot_de_passe(self, mot_de_passe):
        self.password = make_password(mot_de_passe)
    
    def verifier_password(self, mot_de_passe):
        verification = check_password(mot_de_passe)
        return verification



class Notification(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, default="")
    description = models.CharField(max_length=3000)
    lien = models.CharField(max_length=1000, default="")
    date = models.DateField(default=datetime.date.today())
    lue = models.BooleanField(default=False)

        
class Document(models.Model):
    primata = 'primata'
    duplicatatUse = 'duplicatatUse'
    duplicatatPerte = 'duplicatatPerte'

    TYPE_DOCUMENT = [
        (primata, 'primata'),
        (duplicatatUse, 'duplicatatUse'),
        (duplicatatPerte, 'duplicatatPerte'),
    ]
    
    encours = 'encours'
    refuser = 'refuser'
    accepter = 'accepter'
    ETAT_DOCUMENT = [
        (encours, 'encours'),
        (refuser, 'refuser'),
        (accepter, 'accepter'),
    ]
    
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    numCni = models.CharField(max_length=9, blank=True)
    photo =  models.ImageField(upload_to='front/src/lib/image/photo')
    declarationPerte = models.ImageField(upload_to='front/src/lib/image/perte',blank=True)
    certificat = models.ImageField(upload_to='front/src/lib/image/certificat')
    acteNaissance = models.ImageField(upload_to='front/src/lib/image/acte',blank=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    typeDocument = models.CharField(max_length=20, choices=TYPE_DOCUMENT, default=primata)
    etatDocument = models.CharField(max_length=20, choices=ETAT_DOCUMENT, default=encours)
    dateDebut = models.DateField(default=datetime.datetime.now)
    archiver = models.BooleanField(default= False, blank=True)
    

    
class Publication(models.Model):
    photo =  models.ImageField(upload_to='front/src/lib/image/publication', default="", blank=True)
    description = models.TextField(default="")
    aimer = models.IntegerField(null=True, default=0)
    
    
class Commentaire(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenue = models.CharField(max_length=10000)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    
class Reaction(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    liker = models.BooleanField(default=False)
    
class Rendezvou(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    date_fin = models.DateField(default=datetime.datetime.now)
    heure = models.TimeField()
    code = models.CharField(max_length=6)
    recuperer = models.BooleanField(default=False)
    
class Retour(models.Model):
    note = models.IntegerField(default=0)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    
    
class Karatra(models.Model):
    numero = models.CharField(max_length=12)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    
    
