import django_filters
from company.models import Job
class JobFilter(django_filters.FilterSet):
    class Meta:
        model=Job
        fields=["location","description","skills_req"]