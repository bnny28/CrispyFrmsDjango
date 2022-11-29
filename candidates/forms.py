from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator


# Преобразование в нижний регистр
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()


# Преобразование в верхний регистр
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CandidateForm(forms.ModelForm):
    # Валидация
    firstname = forms.CharField(label='Первое имя', min_length=3, max_length=50,  # required=False,
                                validators=[RegexValidator(r'^[а-яА-ЯёЁa-zA-Z\s]*$', message='Только буквы.')],
                                error_messages={'required': 'Это поле должно быть заполнено.', },
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Первое имя',
                                        'style': 'text-transform: capitalize;',
                                        'autocomplete': 'off',
                                    }))
    lastname = forms.CharField(label='Второе имя', min_length=3, max_length=50,
                               validators=[RegexValidator(r'^[а-яА-ЯёЁa-zA-Z\s]*$', message='Только буквы.')],
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Второе имя',
                                       'style': 'text-transform: capitalize;',
                                       'autocomplete': 'off',
                                   }))
    # Применяем свою функцию обработки Uppercase
    job = Uppercase(label='Код специальности', min_length=5, max_length=5,
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'Пример: FR-22',
                            'style': 'text-transform: uppercase;',
                            'autocomplete': 'off',
                            'data-mask': 'AA-00',
                        }))
    # Применяем свою функцию обработки Lowercase
    email = Lowercase(label='Адрес электронной почты', min_length=8, max_length=50,
                      validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$',
                                                 message='Введите правильный адрес электронной почты.')],
                      widget=forms.TextInput(
                          attrs={
                              'placeholder': 'Адрес электронной почты',
                              'style': 'text-transform: lowercase;',
                              'autocomplete': 'off',
                          }))
    # Все что не цифры будет молчаливо сбрасываться если type: number
    # age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Количество лет жизни'}))
    age = forms.CharField(label='Количество лет жизни', min_length=2, max_length=2,
                          validators=[RegexValidator(r'^[0-9]*$', message='Введите целое число.')],
                          error_messages={'required': 'Это поле должно быть заполнено.', },
                          widget=forms.TextInput(attrs={'placeholder': 'Количество лет жизни'}))
    experience = forms.BooleanField(label='Наличие опыта', required=False)  # required=False будет считаться "нет"
    message = forms.CharField(label='О кандидате', min_length=50, max_length=1000, required=False,
                              widget=forms.Textarea(attrs={'placeholder': 'Расскажи немного о себе...', 'rows': 3}))
    file = forms.FileField(label='Резюме', widget=forms.ClearableFileInput())

    # Метод 1
    # GENDER = [('М', 'Мужской'), ('Ж', 'Женский'), ]
    # gender = forms.CharField(label='Пол', widget=forms.RadioSelect(choices=GENDER))

    class Meta:
        model = Candidate
        # fields = '__all__'
        exclude = ['created_at', 'situation']
        # fields = ['firstname', 'lastname', 'email', 'age', 'message']

        # Управление Labels полей
        # labels = {
        #     'gender': 'Ориентация',
        #     'smoker': 'Курильщик',
        # }

        SALARY = (
            ('', 'Ожидаемая месячная зарплата'),
            ('Между ($1000 and $2000)', 'Между ($1000 and $2000)'),
            ('Между ($2000 and $3000)', 'Между ($2000 and $3000)'),
            ('Между ($3000 and $4000)', 'Между ($3000 and $4000)'),
            ('Между ($4000 and $5000)', 'Между ($4000 and $5000)'),
        )

        # Метод 2
        GENDER = [('М', 'Мужской'), ('Ж', 'Женский'), ]

        # Внешние виджеты
        widgets = {
            # Phone (jquery mask)
            'phone': forms.TextInput(attrs={
                # 'style': 'font-size: 15px',  # CSS
                'placeholder': 'Телефон для связи',
                'data-mask': '+7 (000) 000-00-00',
            }),
            # Salary
            'salary': forms.Select(
                choices=SALARY,
                attrs={
                    'class': 'form-control',  # Bootstrap внутри forms.py
                }
            ),
            # Gender
            'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check', }),
            'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check', }),
        }

    # "Супер" функция дает возможность управлять формой переустанавливая опции полей принудительно (временно)
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # ========== ПАНЕЛЬ_УПРАВЛЕНИЯ (ИНДИВИДУАЛЬНЫЕ ВВОДЫ) ==========|
        # Требуется обязательный ввод
        # self.fields['message'].required = True

        # Отключаем возможность ввода (отправить данные невозможно)
        # self.fields['experience'].disabled = True

        # Доступность только для чтения (возможно отправить данные)
        # self.fields['email'].widget.attrs.update({'readonly': 'true'})

        # Установить варианты выбора
        # self.fields['personality'].choices = \
        #     [('', 'Выбери характеристики'), ] + list(self.fields["personality"].choices)[1:]

        # Контроль виджетов
        # self.fields['phone'].widget.attrs.update({
        #     'style': 'font-size: 18px',
        #     'placeholder': 'No phone',
        #     'data-mask': '(000) 000-00-00',
        # })

        # Сообщения ошибок переопределение
        # self.fields['firstname'].error_messages.update({'required': 'Сообщение из суперфункции.'})

        # ========== ПАНЕЛЬ_УПРАВЛЕНИЯ (ГРУППОВЫЕ ВВОДЫ) ==========|
        # 1) Readonly
        # readonly = ['firstname', 'lastname', 'job']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # 2) Disable
        # disabled = ['firstname', 'lastname', 'job']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'

        # 3) Set font
        # font_fields = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality', 'salary', 'message',
        #                'file', 'personality', 'salary', 'gender', 'smoker', 'experience']
        # for field in font_fields:
        #     self.fields[field].widget.attrs['style'] = \
        #         self.fields[field].widget.attrs.setdefault('style', '') + 'font-size: 13px;'

        # 4) Переопределение сообщений об ошибке
        # error_messages = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality', 'salary', 'message',
        #                   'file', 'personality', 'salary', 'gender', 'smoker', 'experience']
        # for field in error_messages:
        #     self.fields[field].error_messages.update({'required': 'Сообщение из суперфункции.'})

        # 5) Выключить автозаполнение полей
        # auto_complete = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality']
        # for field in auto_complete:
        #     self.fields[field].widget.attrs.update({'autocomplete': 'off'})
        # ------------------------------------------------------------------------------

    # Function 1 предотвращающая дублирование кандидатов по адресу почты
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     for obj in Candidate.objects.values_list('email'):
    #         if obj[0] == email:
    #             raise forms.ValidationError(f'Email {email} уже зарегистрирован.')
    #     return email

    # Function 2 предотвращающая дублирование кандидатов по адресу почты
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Email {email} уже зарегистрирован.')
        return email

    # Функция проверки кода в поле работа
    def clean_job(self):
        job = self.cleaned_data.get('job')
        if job == 'FR-22' or job == 'BA-10' or job == 'FU-15':
            return job
        else:
            raise forms.ValidationError(f'Код специальности {job} не является допустимым.')

    # Функция проверки возраста
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < '18' or age > '65':
            raise forms.ValidationError(f'Возраст должен быть между 18 и 65.')
        return age

    # Функция предотвращения неполного значения маски
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 18:
            raise forms.ValidationError(f'Поле не полностью заполнено')
        return phone
