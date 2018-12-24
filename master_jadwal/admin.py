from django.contrib import admin

from .models import subject_offer, time, teamTeaching, dtTeamTeaching, absence, dtAbsence

# Register your models here.

admin.site.register(subject_offer)
admin.site.register(time)
admin.site.register(teamTeaching)
admin.site.register(dtTeamTeaching)
admin.site.register(absence)
admin.site.register(dtAbsence)
