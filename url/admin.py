from django.contrib import admin

from .models import Url


# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = (
        "short_url",
        "alias",
        "link",
    )

    def short_url(self, obj):
        return f"urls.istenith.com/{obj.alias}"

    class Meta:
        model = Url


admin.site.register(Url, Admin)
