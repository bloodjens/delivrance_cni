from django.contrib import admin
from .models import *


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class UtilisateurAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class ArrondissementAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class PublicationAdmin(admin.ModelAdmin):
    readonly_fields=('id',)


admin.site.register(Document, DocumentAdmin)
admin.site.register(Utilisateur,UtilisateurAdmin)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Arrondissement,ArrondissementAdmin)
admin.site.register(Chef)
admin.site.register(Verif)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Commentaire)
admin.site.register(Notification)
admin.site.register(Reaction)
admin.site.register(Rendezvou)
admin.site.register(Retour)
admin.site.register(Karatra)
