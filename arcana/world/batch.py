# -*- coding: utf-8 -*-
 
#HEADER
 
from evennia.objects.models import ObjectDB
 
#CODE
 
#for each in ObjectDB.objects.all():
#    if each.is_typeclass('typeclasses.objects.Object'):
#        each.db.invis = 0

for each in ObjectDB.objects.all():
    if each.is_typeclass('typeclasses.characters.Character'):
        each.db.burned = 0
