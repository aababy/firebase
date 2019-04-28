from datetime import date
 
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from storage.models import App, Category
 
class CategoryFilter(admin.SimpleListFilter):
    title = _('category')
    parameter_name = 'category__name'

    def lookups(self, request, model_admin):
        graphs = model_admin.get_queryset(request)

        for category in Category.objects.all():
            count = graphs.filter(category=category).count()
            display = u"{} ({})".format(category.name, count)
            yield (category, display)

        count = graphs.filter(category=None).count()
        display = u"{} ({})".format('-', count)
        yield ('', display)

    def queryset(self, request, queryset):
        string = self.value()
        if string == None:
            return queryset
        elif string == '':
            return queryset.filter(category=None)
        else:
            return queryset.filter(category__name=string)
 