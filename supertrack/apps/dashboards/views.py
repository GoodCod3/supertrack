from django.views.generic import TemplateView
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from django.db.models.functions import TruncDay, ExtractWeekDay

from supertrack.apps.ticket.models import TicketProductRelationshipModel

WEEKDAY_NAMES = {
    1: "Domingo",
    2: "Lunes",
    3: "Martes",
    4: "Miércoles",
    5: "Jueves",
    6: "Viernes",
    7: "Sábado",
}


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fechas actuales
        now = timezone.now()

        # Semana actual
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # Mes actual
        start_of_month = now.replace(day=1)
        end_of_month = now.replace(month=now.month + 1, day=1) - timedelta(days=1)

        # Mapeo de números a nombres de días de la semana
        weekday_names = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        # Consulta 1: Productos comprados en la semana actual
        products_week = TicketProductRelationshipModel.objects.filter(
            ticket__paid_at__date__range=[start_of_week, end_of_week]
        ).annotate(
            weekday=ExtractWeekDay('ticket__paid_at')  # Extraemos el día de la semana
        ).values(
            'weekday'
        ).annotate(
            total_products=Sum('quantity')
        ).order_by('weekday')

        # Inicializamos una lista con ceros para los productos por cada día de la semana
        week_products = [0] * 7  # Una lista con 7 elementos, uno para cada día de la semana
        for item in products_week:
            # ExtractWeekDay devuelve 1 para Domingo, 2 para Lunes, ..., 7 para Sábado
            # Ajustamos los índices de la lista para que coincidan con Lunes como el primer día
            week_products[(item['weekday'] % 7) - 1] = item['total_products']

        context['products_week'] = {
            "weekdays": weekday_names,
            "products": week_products,
        }

        # Consulta 2: Productos comprados en el mes actual
        products_month = TicketProductRelationshipModel.objects.filter(
            ticket__paid_at__date__range=[start_of_month, end_of_month]
        ).annotate(
            day=TruncDay('ticket__paid_at')
        ).values(
            'day'
        ).annotate(
            total_products=Sum('quantity')
        ).order_by('day')

        # Crear un diccionario de días del mes con valores iniciales en 0
        total_days_in_month = (end_of_month - start_of_month).days + 1
        month_days = [start_of_month + timedelta(days=i) for i in range(total_days_in_month)]
        month_products = [0] * total_days_in_month

        # Llenar la lista con la cantidad de productos comprados en cada día del mes
        for item in products_month:
            day_index = (item['day'] - start_of_month).days  # Obtener el índice correspondiente al día
            month_products[day_index] = item['total_products']

        context['products_month'] = {
            "days": [day.strftime('%Y-%m-%d') for day in month_days],  # Formatear días como YYYY-MM-DD
            "products": month_products,
        }

        # Consulta 3: Tickets con productos comprados durante el mes
        tickets_month = TicketProductRelationshipModel.objects.filter(
            ticket__paid_at__date__range=[start_of_month, end_of_month]
        ).values(
            'ticket__id', 'ticket__paid_at', 'ticket__total', 
            'product__name', 'quantity', 'unit_price', 'total_price'
        ).order_by('ticket__paid_at')

        context['tickets_month'] = tickets_month

        return context
