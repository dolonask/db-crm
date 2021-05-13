from datetime import datetime, timezone

from django.db import models
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

class OwnerShipType(models.Model):
    name = models.CharField("Название", max_length=255)
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма собственности"
        verbose_name_plural = "Формы собственности"


class NumberChoices(models.Model):
    OPTIONS = [
        ('COMPANY', 'Для численности сотрудников компании'),
        ('STRIKE', 'Для численности участников')
    ]

    choice = models.CharField("Выбор", max_length=255)
    is_active = models.BooleanField("Активен", default=True)
    type = models.CharField("Тип", max_length=255, choices=OPTIONS)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Выбор числа"
        verbose_name_plural = "Выбор чисел"


class DemandType(models.Model):
    demand = models.CharField("Требование", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.demand

    class Meta:
        verbose_name = "Тип требования"
        verbose_name_plural = "Типы требований"


class DemandCategory(models.Model):
    name = models.CharField("Название", max_length=255)
    demand_categories = models.ForeignKey('DemandType', on_delete=models.DO_NOTHING, null=True, blank=True,
                                          verbose_name='Тип требования')
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характер требования"
        verbose_name_plural = "Характеры требований"


class Country(models.Model):
    name = models.CharField("Название", max_length=255)
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Region(models.Model):
    name = models.CharField("Название", max_length=255)
    is_active = models.BooleanField("Активен", default=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Source(models.Model):
    name = models.CharField("Название", max_length=100, help_text='Название источника')
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Источник"
        verbose_name_plural = "Источники"


class Company(models.Model):
    name = models.CharField("Название предприятия (юридического лица)", max_length=100)

    company_ownership_type = models.ForeignKey(OwnerShipType, on_delete=models.DO_NOTHING, null=True, blank=True,
                                               verbose_name="Форма собственности компании")

    country_name = models.CharField("Страна происхождения компании", max_length=100)

    company_is_tnk_member = models.BooleanField("Является ли эта кампания частью ТНК (Транснациональная компания)",
                                                default=False)
    company_tnk_name = models.CharField("Название ТНК (Транснациональная компания)",
                                        max_length=100, null=True, blank=True)
    count_workers = models.ForeignKey("NumberChoices", on_delete=models.DO_NOTHING,
                                      null=True, blank=True,
                                      related_name="count_workers",
                                      verbose_name='Общая численность работников на предприятии')


class Card(models.Model):
    ANSWER = [
        ("+", "Да"),
        ("-", "Отсутствует"),
        ("?", "Неизвестно"),
        ("ДР", "Другое")
    ]

    name = models.CharField("Название", max_length=100)
    card_sources = models.ManyToManyField(Source, verbose_name="Источник")
    source_url = models.CharField("Источник информации (ссылка)", max_length=255, null=True, blank=True)
    source_content = models.TextField("Текст статьи/сообщения ", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна")
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name="Регион")
    city_name = models.CharField("Название города", max_length=100)

    company = models.OneToOneField(to=Company, on_delete=models.DO_NOTHING)

    count_strike_participants = models.ForeignKey(NumberChoices, on_delete=models.DO_NOTHING,
                                                  related_name="count_strike_participants",
                                                  verbose_name="Количество участников забастовки/акции")
    card_demand_category = models.ManyToManyField(DemandCategory, verbose_name="Характер требований")
    date_strike_start = models.DateTimeField("Дата начало проведения забастовки/акции",
                                             default=datetime(year=2020, month=1, day=1, hour=8, tzinfo=timezone.utc))
    data_strike_end = models.DateTimeField("Дата конца проведения забастовки/акции",
                                           default=datetime(year=2020, month=1, day=1, hour=12, tzinfo=timezone.utc))
    has_trade_union = models.CharField("Профсоюз", choices=ANSWER, max_length=50, blank=False, default='+')
    card_create_date = models.DateTimeField("Дата начала", auto_now_add=True)
    card_end_date = models.DateTimeField("Дата завершения", default=datetime(year=2999,
                                                                             month=1, day=1, tzinfo=timezone.utc))
    last_update = models.DateTimeField("Дата последнего изменения", auto_now=True)
    is_active = models.BooleanField("Активен", default=True)

    THE_NATURE_OF_THE_GROUP = [
        ('Б/ПГ', 'Бригада или производственная группа'),
        ('опр категория', 'Определенная категория работников'),
        ('Др', 'Другое'),
    ]

    TRADE_UNION_MEMBERSHIP = [
        ('Все', 'Все состоят в профсоюзе'),
        ('Не все', 'В профсоюзе состоят не все'),
        ('Никто', 'Никто не состоит в профсоюзе'),
    ]

    GENDER = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]

    AGE = [
        ('<18', 'менее 18 лет'),
        ('19-62', '19-62'),
        ('> 63', '63 и старше'),
    ]

    trade_union = models.CharField("Название профсоюза", max_length=200, default="")
    phone_number_union = models.CharField("Контакты", max_length=200, blank=True, null=True)
    address_union = models.CharField("Адрес", max_length=200, blank=True, null=True)
    group = models.CharField("Группа лиц", choices=THE_NATURE_OF_THE_GROUP, max_length=200, default='Б/ПГ')
    union_membership = models.CharField("Членство в профсоюзе", choices=TRADE_UNION_MEMBERSHIP, max_length=200,
                                        default='Все')
    first_name = models.CharField("Имя", max_length=50, blank=True, null=True)
    last_name = models.CharField("Фамилия", max_length=50, blank=True, null=True)
    gender = models.CharField("Пол", max_length=1, choices=GENDER, default='М')
    age = models.CharField("Возраст", max_length=10, choices=AGE, default='<18')
    profession = models.CharField("Профессия", max_length=100, default="")
    employer = models.CharField('Работодатель', max_length=200, default="")
    phone_number_employer = models.CharField("Контакты", max_length=200, blank=True, null=True)
    address_employer = models.CharField("Адрес", max_length=200, blank=True, null=True)

    ANSWER = [
        ('-', 'Кратковременная'),
        ('---', 'Длящаяся')
    ]
    ANSWER2 = [
        ('+', 'удовлетворены'),
        ('-', 'не удовлетворены'),
        ('+-', 'удовлетворены частично')
    ]
    duration = models.CharField('Длительность забастовки/акции', max_length=3, choices=ANSWER, default='-')
    meeting_requirements = models.CharField('Удовлетворение требований', max_length=2, choices=ANSWER2, default='+')
    story = models.TextField('Укажите ПОСЛЕДОВАТЕЛЬНО, что произошло',
                             help_text='Параллельно указывайте, чем подтверждаются эти факты (если есть приложения,'
                                       ' укажите сразу номера и названия соответствующих приложений)', default="")
    reasons_for_strike = models.TextField('Причины начала забастовки',
                                          help_text='Опишите причины начала забастовки (например: условия труда на '
                                                    'предприятии, продолжительность рабочего времени, безопасность и'
                                                    'т.д. время, связанное с работой)', default="")
    change_number_participants = models.TextField('Как менялось количество участников забастовки',
                                                  help_text='Опишите как менялось количество участников '
                                                            'забастовки во время проведения и что на это влияло?',
                                                  default="")
    initiators_and_participants = models.TextField('Что с инициаторами и участниками',
                                                   help_text="Ситуация с инициаторами и участниками забастовки/акции"
                                                             " (продолжают ли они работать, применялись ли к ним административные"
                                                             " меры со стороны предприятия)", default="")
    state_position = models.TextField("Позиция государства (Опишите реакцию государственных органов)", default="")
    results_so_far = models.TextField("C какими итогами закончилась забастовка, "
                                      "если еще не закончилась, то какие итоги на данный момент.", default="")
    additional_information = models.TextField("Любая дополнительная информация", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
