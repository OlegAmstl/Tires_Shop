from django.views.generic import ListView
from .models import Tire

class TireListView(ListView):
    """
    Отображает список всех шин.

    Attributes:
    - model: Модель шин, которую представляет эта вьюха.
    - template_name: Путь к шаблону, который будет использоваться для отображения списка шин.
    - context_object_name: Имя переменной, в которую будет помещен список шин в шаблоне.
    - paginate_by: Количество шин, отображаемых на одной странице.

    Methods:
    - get_queryset: Переопределяет метод родительского класса для фильтрации и сортировки списка шин.
    - get_context_data: Переопределяет метод родительского класса для добавления дополнительных контекстных данных в шаблон.
    """
    model = Tire
    template_name = 'catalog/tire_list.html'
    context_object_name = 'tires'
    paginate_by = 28  # Показывать 28 шин на странице
