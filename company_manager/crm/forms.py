from django.forms import ModelForm, ValidationError
from crm.models import Employee, Company
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('department', 'phone_number')


class CompanyForm(ModelForm):
    def clean_identification_number(self):
        identification_number = self.cleaned_data['identification_number']

        if len(identification_number) != 8:
            raise ValidationError(_("The identification number has incorrect length."))
        return identification_number

    class Meta:
        model = Company
        fields = ["name", "status", "phone_number", "email", "identification_number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="col-sm-4"),
                Div("status", css_class="col-sm-2"),
                Div("identification_number", css_class="col-sm-4"),
                Div("email", css_class="col-sm-4"),
                Div("phone_number", css_class="col-sm-4"),
                css_class="row",
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button')
            )
        )
