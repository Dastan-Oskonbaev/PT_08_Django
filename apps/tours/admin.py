from django.contrib import admin

from apps.tours.models import PlaceCategory, Place, Review

# admin.site.register(PlaceCategory)
admin.site.register(Review)

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


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'views_count', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('name', 'category__name', 'id')
    list_display_links = ('id', 'name')
    ordering = ('-id',)



