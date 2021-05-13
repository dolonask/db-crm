from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Card, Region
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django import forms


class CommonFormHelper(FormHelper):
    def __init__(self):
        super(CommonFormHelper, self).__init__()
        self.disable_csrf = True
        self.form_tag = False


class CardForm(ModelForm):
    # regions = forms.ModelChoiceField(queryset=Regions.objects.all())
    # documents = forms.ModelMultipleChoiceField(queryset=Documents.objects.all())
    class Meta:
        model = Card

        # fields = ['card_sources', 'source_url', 'source_content', 'regions',
        #           'city_name', 'company', 'company_ownership_type', 'company_country',
        #           'company_is_tnk_member', 'company_tnk_name', 'count_workers', 'count_strike_participants',
        #           'card_demand_category', 'data_strike_end', 'has_trade_union',
        #           'is_active', 'trade_union', 'phone_number_union',
        #           'address_union', 'group', 'union_membership', 'first_name', 'last_name', 'gender',
        #           'age', 'profession', 'employer', 'phone_number_employer', 'address_employer',
        #           'duration', 'meeting_requirements', 'story', 'reasons_for_strike', 'change_number_participants',
        #           'initiators_and_participants', 'state_position', 'results_so_far', 'additional_information']

        # fields = '__all__'

        fields = [
            'name', 'card_sources', 'source_url', 'source_content', 'country', 'region','city_name', 'company',
            'company_ownership_type'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-select'}),
            'card_sources': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list-none', 'id': 'card_sources'}),
            'card_demand_category': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'card_demand_category'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            # 'region': forms.ModelChoiceField(queryset=Region.objects.all(),attrs={'class': 'form-control'}),

            # 'source_url': forms.TextInput(attrs={'style': 'display: none', 'id': 'source_url'}),
            'source_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'source_url'}),
            # 'source_content': forms.TextInput(attrs={'style': 'display: none', 'id': 'source_con'}),
            'source_content': forms.Textarea(attrs={'class': 'form-control', 'id': 'source_con'}),

            'city_name': forms.TextInput(attrs={'class': 'form-select'}),
            'company': forms.TextInput(attrs={'class': 'form-select'}),
            'company_ownership_type': forms.Select(attrs={'class': 'form-control', 'id': 'company_ownership_type'}),
            'company_country': forms.Select(
                attrs={'class': 'form-control', 'style': 'display: none', 'id': 'company_country'}),
            'company_is_tnk_member': forms.CheckboxInput(
                attrs={'class': 'form-check-label', 'style': 'display: none', 'id': 'company_is_tnk_member'}),
            'company_tnk_name': forms.TextInput(attrs={'class': 'form-select'}),
            'count_workers': forms.Select(attrs={'class': 'form-control'}),
            'count_strike_participants': forms.Select(attrs={'class': 'form-control'}),
            'data_strike_end': forms.DateTimeInput(),
            'has_trade_union': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'trade_union': forms.TextInput(attrs={'class': 'form-select'}),
            'phone_number_union': forms.TextInput(attrs={'class': 'form-select'}),
            'address_union': forms.TextInput(attrs={'class': 'form-select'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'union_membership': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-select'}),
            'last_name': forms.TextInput(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-select'}),
            'employer': forms.TextInput(attrs={'class': 'form-select'}),
            'phone_number_employer': forms.TextInput(attrs={'class': 'form-select'}),
            'address_employer': forms.TextInput(attrs={'class': 'form-select'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'meeting_requirements': forms.Select(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
        #     self.helper_name_info = CommonFormHelper()
        #     self.helper_name_info.layout = Layout(
        #         Tab(
        #             'Name',
        #             'name', 'card_sources',
        #         ),
        #     )
        #
        #     self.helper_location_info = CommonFormHelper()
        #     self.helper_location_info.layout = Layout(
        #         Tab(
        #             'Address',
        #             'source_url', 'source_content',
        #         ),
        #     )
        #
        #     super(CardForm, self).__init__(*args, **kwargs)
