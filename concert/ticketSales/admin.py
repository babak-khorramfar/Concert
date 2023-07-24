from django.contrib import admin
from .models import concertModel, ticketModel, timeModel, locationModel

# Register models.
admin.site.register(concertModel)
admin.site.register(ticketModel)
admin.site.register(timeModel)
admin.site.register(locationModel)
