from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from app_employment.models import Vacancy

@permission_required('app_employment.view_vacancy')
def vacancy_list(request):
    """
    Проверка прав прошла успешно, рендерим страничку, иначе показываем ошибку.
    #<app>.<action>_<object_name>
    """

    vacancy = Vacancy.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancy})


