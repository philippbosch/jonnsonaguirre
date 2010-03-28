from django.contrib import admin

from jonnsonaguirre.works.models import Work, MediaFile



class MediaFileInline(admin.TabularInline):
    model = MediaFile
    exclude = ('name',)

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','date',)
    ordering = ('name',)
    inlines = (MediaFileInline,)
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Work, WorkAdmin)
