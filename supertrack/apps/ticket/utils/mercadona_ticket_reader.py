import re
from datetime import datetime

import pdfplumber


def get_mercadona_ticket_info(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[0]
            texto = page.extract_text()
            lines = texto.split("\n")

            products = []
            total = None
            purchase_date = None

            # Regular expression to capture products, prices and amounts
            product_pattern = re.compile(
                r"(\d+)\s+([\w\s]+)\s+([\d,]+\s*€?)\s*([\d,]+\s*€?)?"
            )

            for line in lines:
                # Getting purchase date
                if "OP:" in line:
                    purchase_date = re.search(
                        r"\d{2}/\d{2}/\d{4}", line
                    ).group(0)
                    purchase_date = datetime.strptime(
                        purchase_date, "%d/%m/%Y"
                    ).strftime("%Y-%m-%d")

                # Finding products and prices
                match = product_pattern.search(line)
                if match:
                    quantity = match.group(1)
                    product_name = match.group(2).strip()
                    unit_price = (
                        match.group(3)
                        .replace(",", ".")
                        .replace("€", "")
                        .strip()
                    )
                    total_price = (
                        match.group(4) if match.group(4) else unit_price
                    )
                    total_price = (
                        total_price.replace(",", ".").replace("€", "").strip()
                    )

                    products.append(
                        {
                            "quantity": quantity,
                            "name": product_name,
                            "unit_price": float(unit_price),
                            "total_price": float(total_price),
                        }
                    )

                # Total purchase
                if "TOTAL (€)" in line:
                    total = float(line.split()[-1].replace(",", "."))

            return {
                "purchase_date": purchase_date,
                "products": products,
                "total": total,
            }
    except Exception:
        pass
