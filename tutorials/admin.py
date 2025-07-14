from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Vedios)
class VedioAdmin(admin.ModelAdmin):
    list_display =('identifier',)
class TeachSubjectInline(admin.TabularInline):
    model = UnitAndTutorial
    extra = 2 # how many rows to show
class UnitChapterInline(admin.TabularInline):
    model = UnitAndChapter
    extra = 2
     # how many rows to show
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('identifier',)
class UnitAdmin(admin.ModelAdmin):
    list_display=('identifier',)
    inlines = (UnitChapterInline,)
class SchoolClassAdmin(admin.ModelAdmin):
    inlines = (TeachSubjectInline,)
admin.site.register(collection)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Unit,UnitAdmin)
admin.site.register(tutorial,SchoolClassAdmin)
admin.site.register(Request)