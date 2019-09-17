from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from .models import testCase
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
# admin.site.register(Tutorial)
admin.site.register(testCase)

class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		("title/data", {"fields":["tutorial_title","tutorial_published"]}),
		("URL", {"fields":["tutorial_slug"]}),
		("Series", {"fields":["tutorial_series"]}),
		("Content", {"fields":["tutorial_content"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
