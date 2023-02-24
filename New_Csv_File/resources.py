from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import Country, Hobby, PersonDetail, Skill
class PersonDetailsAdminResource(resources.ModelResource):

    user = fields.Field(column_name='user', attribute='user', widget=ForeignKeyWidget(User, field='username'))
    country = fields.Field(column_name='country', attribute='country', widget=ForeignKeyWidget(Country, field='name'))
    hobby = fields.Field(column_name='hobby', attribute='hobby', widget=ForeignKeyWidget(Hobby, field='name'))
    skill = fields.Field(column_name='skill', attribute='skill', widget=ForeignKeyWidget(model=Skill,field='name'))
  
    class Meta:
        model = PersonDetail
        fields = (
            'id',
            'user',
            'name',
            'gender',
            'dob',
            'mobile',
            'email',
            'aadhaar',
            'country',
            'address',
            'hobby',
            'skill'
        )