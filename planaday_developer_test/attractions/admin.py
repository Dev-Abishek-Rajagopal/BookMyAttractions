from django.contrib import admin
from .models import Attraction, Inventory, Booking

# Register your models here.
@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "created"]
    search_fields = ["name"]

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["attraction", "id", "tickets","remain_tickets"]
    search_fields = ["attraction"]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["attraction", "id", "date","noftickets","user"]
    search_fields = ["attraction"]