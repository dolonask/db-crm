# Generated by Django 3.2.2 on 2021-05-13 07:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0002_country_demandcategory_demandtype_region_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='countries',
            new_name='country',
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название предприятия (юридического лица)')),
                ('country_name', models.CharField(max_length=100, verbose_name='Страна происхождения компании')),
                ('company_is_tnk_member', models.BooleanField(default=False, verbose_name='Является ли эта кампания частью ТНК (Транснациональная компания)')),
                ('company_tnk_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название ТНК (Транснациональная компания)')),
                ('company_ownership_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='strike.ownershiptype', verbose_name='Форма собственности компании')),
                ('count_workers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='count_workers', to='strike.numberchoices', verbose_name='Общая численность работников на предприятии')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('source_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Источник информации (ссылка)')),
                ('source_content', models.TextField(blank=True, null=True, verbose_name='Текст статьи/сообщения ')),
                ('city_name', models.CharField(max_length=100, verbose_name='Название города')),
                ('date_strike_start', models.DateTimeField(default=datetime.datetime(2020, 1, 1, 8, 0, tzinfo=utc), verbose_name='Дата начало проведения забастовки/акции')),
                ('data_strike_end', models.DateTimeField(default=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=utc), verbose_name='Дата конца проведения забастовки/акции')),
                ('has_trade_union', models.CharField(choices=[('+', 'Да'), ('-', 'Отсутствует'), ('?', 'Неизвестно'), ('ДР', 'Другое')], default='+', max_length=50, verbose_name='Профсоюз')),
                ('card_create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')),
                ('card_end_date', models.DateTimeField(default=datetime.datetime(2999, 1, 1, 0, 0, tzinfo=utc), verbose_name='Дата завершения')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('trade_union', models.CharField(default='', max_length=200, verbose_name='Название профсоюза')),
                ('phone_number_union', models.CharField(blank=True, max_length=200, null=True, verbose_name='Контакты')),
                ('address_union', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('group', models.CharField(choices=[('Б/ПГ', 'Бригада или производственная группа'), ('опр категория', 'Определенная категория работников'), ('Др', 'Другое')], default='Б/ПГ', max_length=200, verbose_name='Группа лиц')),
                ('union_membership', models.CharField(choices=[('Все', 'Все состоят в профсоюзе'), ('Не все', 'В профсоюзе состоят не все'), ('Никто', 'Никто не состоит в профсоюзе')], default='Все', max_length=200, verbose_name='Членство в профсоюзе')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('gender', models.CharField(choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], default='М', max_length=1, verbose_name='Пол')),
                ('age', models.CharField(choices=[('<18', 'менее 18 лет'), ('19-62', '19-62'), ('> 63', '63 и старше')], default='<18', max_length=10, verbose_name='Возраст')),
                ('profession', models.CharField(default='', max_length=100, verbose_name='Профессия')),
                ('employer', models.CharField(default='', max_length=200, verbose_name='Работодатель')),
                ('phone_number_employer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Контакты')),
                ('address_employer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('duration', models.CharField(choices=[('-', 'Кратковременная'), ('---', 'Длящаяся')], default='-', max_length=3, verbose_name='Длительность забастовки/акции')),
                ('meeting_requirements', models.CharField(choices=[('+', 'удовлетворены'), ('-', 'не удовлетворены'), ('+-', 'удовлетворены частично')], default='+', max_length=2, verbose_name='Удовлетворение требований')),
                ('story', models.TextField(default='', help_text='Параллельно указывайте, чем подтверждаются эти факты (если есть приложения, укажите сразу номера и названия соответствующих приложений)', verbose_name='Укажите ПОСЛЕДОВАТЕЛЬНО, что произошло')),
                ('reasons_for_strike', models.TextField(default='', help_text='Опишите причины начала забастовки (например: условия труда на предприятии, продолжительность рабочего времени, безопасность ит.д. время, связанное с работой)', verbose_name='Причины начала забастовки')),
                ('change_number_participants', models.TextField(default='', help_text='Опишите как менялось количество участников забастовки во время проведения и что на это влияло?', verbose_name='Как менялось количество участников забастовки')),
                ('initiators_and_participants', models.TextField(default='', help_text='Ситуация с инициаторами и участниками забастовки/акции (продолжают ли они работать, применялись ли к ним административные меры со стороны предприятия)', verbose_name='Что с инициаторами и участниками')),
                ('state_position', models.TextField(default='', verbose_name='Позиция государства (Опишите реакцию государственных органов)')),
                ('results_so_far', models.TextField(default='', verbose_name='C какими итогами закончилась забастовка, если еще не закончилась, то какие итоги на данный момент.')),
                ('additional_information', models.TextField(blank=True, null=True, verbose_name='Любая дополнительная информация')),
                ('card_demand_category', models.ManyToManyField(to='strike.DemandCategory', verbose_name='Характер требований')),
                ('card_sources', models.ManyToManyField(to='strike.Source', verbose_name='Источник')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='strike.company')),
                ('count_strike_participants', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='count_strike_participants', to='strike.numberchoices', verbose_name='Количество участников забастовки/акции')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='strike.country', verbose_name='Страна')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='strike.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
            },
        ),
    ]
