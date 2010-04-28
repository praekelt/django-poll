from django.contrib import admin

from poll.models import Poll, PollOption
from content.admin import ModelBaseAdmin


admin.site.register(Poll, ModelBaseAdmin)
admin.site.register(PollOption, ModelBaseAdmin)