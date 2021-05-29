from django.contrib import admin
from root_app.models import Provider, Project, Attribute, Atom, Criteria, Pricing, Rule
admin.site.register(Provider)
admin.site.register(Project)
admin.site.register(Attribute)
admin.site.register(Atom)
admin.site.register(Criteria)
admin.site.register(Pricing)
admin.site.register(Rule)
# Register your models here.
