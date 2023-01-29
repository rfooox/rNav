from django.contrib import admin
from weblist.models import WebType, WebTag, WebList


# Register your models here.

class WebTypeAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_time', 'edited_time')
    list_display = ('id', 'web_type', 'web_seq', 'edited_time')

    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)


class WebTagAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_time', 'edited_time')
    list_display = ('id', 'web_tag', 'web_seq', 'edited_time')

    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)


class WebListAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_time', 'edited_time')
    list_display = ('id', 'web_title', 'web_type', 'get_web_tag', 'web_icon', 'web_url', 'web_description')

    def get_web_tag(self, obj):
        tag_list = []
        for t in obj.tag.all():
            tag_list.append(t.web_tag)
        return ','.join(tag_list)

    get_web_tag.short_description = "标签"

    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(WebList, WebListAdmin)
admin.site.register(WebType, WebTypeAdmin)
admin.site.register(WebTag, WebTagAdmin)
