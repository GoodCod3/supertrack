import calendar
import base64
from datetime import timedelta, datetime
from django.views.generic import TemplateView
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import TruncDay, ExtractWeekDay
from django.contrib.auth.mixins import LoginRequiredMixin

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


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def _get_current_week_data(self):
        now = timezone.now()

        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        weekday_names = [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
        ]

        products_week = (
            TicketProductRelationshipModel.objects.filter(
                ticket__paid_at__date__range=[start_of_week, end_of_week]
            )
            .annotate(weekday=ExtractWeekDay("ticket__paid_at"))
            .values("weekday")
            .annotate(total_products=Sum("total_price"))
            .order_by("weekday")
        )

        week_products = [0] * 7
        for item in products_week:
            week_products[(item["weekday"] % 7) - 1] = item["total_products"]

        return {
            "weekdays": weekday_names,
            "products": week_products,
            "current_week_start": start_of_week,
            "current_week_end": end_of_week,
        }

    def _get_date_range(self):
        def get_first_day(date):
            return datetime(date.year, date.month, 1)


        def get_last_day(date):
            return datetime(
                date.year, date.month, calendar.monthrange(date.year, date.month)[1]
            )
        today = timezone.now().date()

        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")

        if start_date and end_date:
            try:
                start_of_range = datetime.strptime(
                    start_date, "%Y-%m-%d"
                ).date()
                end_of_range = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                start_of_range = get_first_day(today)
                end_of_range = get_last_day(today)
        else:
            start_of_range = get_first_day(today)
            end_of_range = get_last_day(today)

        return start_of_range, end_of_range

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        start_of_month, end_of_month = self._get_date_range()

        context["products_week"] = self._get_current_week_data()

        products_month = (
            TicketModel.objects.filter(
                paid_at__date__range=[start_of_month, end_of_month]
            )
            .annotate(day=TruncDay("paid_at"))
            .values("day")
            .annotate(total_amount=Sum("total"))
            .order_by("day")
        )

        # Create a dictionary of days of the month with initial values ​​at 0
        total_days_in_month = (end_of_month - start_of_month).days + 1
        month_days = [
            start_of_month + timedelta(days=i)
            for i in range(total_days_in_month)
        ]
        month_products = [0] * total_days_in_month

        # Fill in the list with the quantity of products purchased on each day of the month
        for item in products_month:
            day_index = (item["day"].date() - start_of_month).days
            month_products[day_index] = item["total_amount"]

        context["products_month"] = {
            "days": [day.strftime("%d") for day in month_days],
            "products": month_products,
        }

        tickets_month = (
            TicketModel.objects.filter(
                paid_at__date__range=[start_of_month, end_of_month]
            )
            .prefetch_related("ticketproductrelationshipmodel_set")
            .order_by("paid_at")
        )

        tickets_data = []
        total_tickets_month = 0
        for ticket in tickets_month:
            total_tickets_month += ticket.total
            ticket_pdf = ticket.image.path if ticket.image else None
            if ticket_pdf:
                pdf_content = None
                with open(ticket_pdf, "rb") as pdf_file:
                    # Convert pdf to a string
                    pdf_content = base64.b64encode(pdf_file.read()).decode()
            ticket_info = {
                "total": ticket.total,
                "id": ticket.pk,
                "paid_at": ticket.paid_at.strftime("%Y-%m-%d"),
                "pdf": pdf_content,
                "products": [],
            }
            for product_rel in ticket.ticketproductrelationshipmodel_set.all():
                product_info = {
                    "name": product_rel.product.name,
                    "quantity": product_rel.quantity,
                    "unit_price": product_rel.unit_price,
                    "total_price": product_rel.total_price,
                }
                ticket_info["products"].append(product_info)

            tickets_data.append(ticket_info)

        context["tickets_month"] = tickets_data
        context["total_tickets_month"] = "%.2f" % total_tickets_month
        context["start_of_month"] = start_of_month
        context["end_of_month"] = end_of_month

        return context
