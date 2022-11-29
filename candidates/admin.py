from django.contrib import admin
from django.utils.html import format_html
from .models import Candidate
from .forms import CandidateForm


class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {'smoker': admin.HORIZONTAL}
    form = CandidateForm
    readonly_fields = ['experience', 'firstname', 'lastname', 'job', 'email', 'age', 'phone', 'salary', 'personality',
                       'gender', 'smoker', 'file', 'frameworks', 'languages', 'mobile', 'libraries', 'others',
                       'databases', 'message', ]
    exclude = ['согласование']
    list_filter = ['situation']
    list_display = ['name', 'job', 'email', 'age', 'created_at', 'согласование', '_']
    search_fields = ['firstname', 'lastname', 'email', 'age', 'situation']
    list_per_page = 10

    # Функция для скрытия имени и фамилии - используем суперфункцию системы
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove('firstname')
            fields.remove('lastname')
        return fields

    # Функция смены значков в панели для поля situation
    def _(self, obj):
        if obj.situation == 'Одобрен':
            return True
        elif obj.situation == 'На рассмотрении':
            return None
        else:
            return False

    _.boolean = True

    # Функция смены цвета шрифта в панели для поля situation
    def согласование(self, obj):
        if obj.situation == 'Одобрен':
            color = '#28a645'
        elif obj.situation == 'На рассмотрении':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html(f'<strong><p style="color: {color}">{obj.situation}</p></strong>')

    согласование.allow_tags = True


admin.site.register(Candidate, CandidateAdmin)
