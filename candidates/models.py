from django.db import models
from multiselectfield import MultiSelectField

SITUATION = (
    ('На рассмотрении', 'На рассмотрении'),
    ('Одобрен', 'Одобрен'),
    ('Отклонен', 'Отклонен'),
)

PERSONALITY = (
    ('', 'Выбери характеристики'),
    ('Открытый', 'Открытый'),
    ('Экстраверт', 'Экстраверт'),
    ('Интроверт', 'Интроверт'),
    ('Сдержанный', 'Сдержанный'),
    ('Серьезный', 'Серьезный'),
)

SMOKER = (
    ('1', 'Да'),
    ('0', 'Нет'),
)

# Multiple Checkboxes
FRAMEWORKS = (
    ('Laravel', 'Laravel'),
    ('Angular', 'Angular'),
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('Vue', 'Vue'),
    ('Others', 'Others'),
)
LANGUAGES = (
    ('Python', 'Python'),
    ('Javascript', 'Javascript'),
    ('Java', 'Java'),
    ('C++', 'C++'),
    ('Ruby', 'Ruby'),
    ('Others', 'Others'),
)
DATABASES = (
    ('MySql', 'MySql'),
    ('Postgree', 'Postgree'),
    ('MongoDB', 'MongoDB'),
    ('SqLite3', 'SqLite3'),
    ('Oracle', 'Oracle'),
    ('Others', 'Others'),
)
LIBRARIES = (
    ('Ajax', 'Ajax'),
    ('Jquery', 'Jquery'),
    ('React.js', 'React.js'),
    ('Chart.js', 'Chart.js'),
    ('Gsap', 'Gsap'),
    ('Others', 'Others'),
)
MOBILE = (
    ('React native', 'React native'),
    ('Kivy', 'Kivy'),
    ('Flutter', 'Flutter'),
    ('Ionic', 'Ionic'),
    ('Xamarin', 'Xamarin'),
    ('Others', 'Others'),
)
OTHERS = (
    ('UML', 'UML'),
    ('SQL', 'SQL'),
    ('Docker', 'Docker'),
    ('Git', 'Git'),
    ('GraphQL', 'GraphQL'),
    ('Others', 'Others'),
)


class Candidate(models.Model):
    firstname = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Фамилия', max_length=50)
    job = models.CharField('Код специальности', max_length=5)
    age = models.CharField('Возраст', max_length=3)
    phone = models.CharField('Телефон', max_length=25)
    personality = models.CharField('Личностные характеристики', max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField('Вилка зарплаты', max_length=50)
    gender = models.CharField('Пол', max_length=10)
    experience = models.BooleanField('Наличие опыта', null=True)
    smoker = models.CharField('Курит', max_length=10, choices=SMOKER, default='')
    email = models.EmailField('Эл.почта', max_length=50)
    message = models.TextField('Сообщение')
    file = models.FileField('Резюме')
    created_at = models.DateTimeField('Создание', auto_now_add=True)
    situation = models.CharField('Согласование', max_length=50, null=True, choices=SITUATION, default='На рассмотрении')
    company_note = models.TextField('Заметки согласования', blank=True)
    # Multiple Checkboxes
    frameworks = MultiSelectField('Фреймворки', choices=FRAMEWORKS, max_length=200, default='')
    languages = MultiSelectField('Языки', choices=LANGUAGES, max_length=200, default='')
    databases = MultiSelectField('Базы данных', choices=DATABASES, max_length=200, default='')
    libraries = MultiSelectField('Библиотеки', choices=LIBRARIES, max_length=200, default='')
    mobile = MultiSelectField('Мобильная разработка', choices=MOBILE, max_length=200, default='')
    others = MultiSelectField('Другое', choices=OTHERS, max_length=200, default='')

    # С заглавной буквы (Имя и Фамилия)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    # Объединение имени и фамилии в форме админки
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    # Объединение имени и фамилии в представлении админки
    def name(self):
        return "%s %s" % (self.firstname, self.lastname)



