import base64
from django.views.generic import TemplateView
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from django.db.models.functions import TruncDay, ExtractWeekDay

from supertrack.apps.ticket.models import (
    TicketProductRelationshipModel,
    TicketModel,
)

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
        end_of_month = now.replace(month=now.month + 1, day=1) - timedelta(
            days=1
        )

        # Mapeo de números a nombres de días de la semana
        weekday_names = [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
        ]

        # Consulta 1: Productos comprados en la semana actual
        products_week = (
            TicketProductRelationshipModel.objects.filter(
                ticket__paid_at__date__range=[start_of_week, end_of_week]
            )
            .annotate(
                weekday=ExtractWeekDay(
                    "ticket__paid_at"
                )  # Extraemos el día de la semana
            )
            .values("weekday")
            .annotate(total_products=Sum("total_price"))
            .order_by("weekday")
        )

        # Inicializamos una lista con ceros para los productos por cada día de la semana
        week_products = [
            0
        ] * 7  # Una lista con 7 elementos, uno para cada día de la semana
        for item in products_week:
            # ExtractWeekDay devuelve 1 para Domingo, 2 para Lunes, ..., 7 para Sábado
            # Ajustamos los índices de la lista para que coincidan con Lunes como el primer día
            week_products[(item["weekday"] % 7) - 1] = item["total_products"]

        context["products_week"] = {
            "weekdays": weekday_names,
            "products": week_products,
        }

        # Consulta 2: Productos comprados en el mes actual
        products_month = (
            TicketProductRelationshipModel.objects.filter(
                ticket__paid_at__date__range=[start_of_month, end_of_month]
            )
            .annotate(day=TruncDay("ticket__paid_at"))
            .values("day")
            .annotate(total_products=Sum("total_price"))
            .order_by("day")
        )

        # Crear un diccionario de días del mes con valores iniciales en 0
        total_days_in_month = (end_of_month - start_of_month).days + 1
        month_days = [
            start_of_month + timedelta(days=i)
            for i in range(total_days_in_month)
        ]
        month_products = [0] * total_days_in_month

        # Llenar la lista con la cantidad de productos comprados en cada día del mes
        for item in products_month:
            day_index = (
                item["day"] - start_of_month
            ).days  # Obtener el índice correspondiente al día
            month_products[day_index] = item["total_products"]

        context["products_month"] = {
            "days": [
                day.strftime("%d") for day in month_days
            ],  # Formatear días como YYYY-MM-DD
            "products": month_products,
        }

        tickets_month = (
            TicketModel.objects
            .filter(paid_at__date__range=[start_of_month, end_of_month])
            .prefetch_related('ticketproductrelationshipmodel_set')
            .order_by('paid_at')
        )

        tickets_data = []
        total_tickets_month = 0
        for ticket in tickets_month:
            total_tickets_month += ticket.total
            ticket_pdf = ticket.image.path if ticket.image else None
            if ticket_pdf:
                pdf_content = None
                with open(ticket_pdf, 'rb') as pdf_file:
                    # Convert pdf to a string
                    pdf_content = base64.b64encode(pdf_file.read()).decode()
            ticket_info = {
                'total': ticket.total,
                'id': ticket.pk,
                'paid_at': ticket.paid_at.strftime('%Y-%m-%d'),
                'pdf': pdf_content,
                'products': []
            }
            for product_rel in ticket.ticketproductrelationshipmodel_set.all():
                product_info = {
                    'name': product_rel.product.name,
                    'quantity': product_rel.quantity,
                    'unit_price': product_rel.unit_price,
                    'total_price': product_rel.total_price
                }
                ticket_info['products'].append(product_info)

            tickets_data.append(ticket_info)

        context["tickets_month"] = tickets_data
        context["total_tickets_month"] = "%.2f" % total_tickets_month

        return context
