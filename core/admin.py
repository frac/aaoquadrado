from django.db.models import Q
from django.contrib import admin
from django.contrib.auth.models import User
from models import *
import datetime

"""
class PhotoInline(admin.TabularInline):
        model = Photo
        extra = 1


class MeasurementInline(admin.TabularInline):
        model = Measurement
        extra = 10


def publish(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.published_at:
            obj.published_at=datetime.datetime.today()
            obj.save()


def use_photo(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.used:
            obj.used=True
            obj.save()

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [MeasurementInline]
    list_display = ('title', 'wave','pic','slug', 'tags','published_at')
    ordering = ('-published_at',)
    actions = [publish]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pic":
            kwargs["queryset"] = Photo.objects.filter(Q(used=False) | Q(post__isnull=False)).distinct()
            return db_field.formfield(**kwargs)
        return super(RecipeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','pic','slug','published_at')
    ordering = ('-published_at',)
    actions = [publish]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pic":
            kwargs["queryset"] = Photo.objects.filter(Q(used=False) | Q(post__isnull=False)).distinct()
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','pic',)
    ordering = ('pic',)



class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','used','full_url', 'wave')
    actions = [use_photo]
"""
def convidado_do_dri(modeladmin, request, queryset):
    for obj in queryset:
        obj.dequem=1
        obj.save()

def convidado_da_li(modeladmin, request, queryset):
    for obj in queryset:
        obj.dequem=2
        obj.save()

class ConviteAdmin(admin.ModelAdmin):
    list_display = ('nome','email','convidados', 'convites', 'dequem')
    ordering = ('dequem',)
    actions = [convidado_do_dri,convidado_da_li]

admin.site.register(Convite, ConviteAdmin)
