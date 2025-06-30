from django.contrib import admin

from apps.tours.models import PlaceCategory, Place

# admin.site.register(PlaceCategory)
# admin.site.register(Place)

@admin.register(PlaceCategory)
class PlaceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name', 'id')
    list_display_links = ('id', 'name')
    ordering = ('-id',)

    fieldsets = (
        ('Основное название', {
            'fields': ('name', )
        }),
        ('Доп название', {
            'fields': ('short_description',)
        }),
    )