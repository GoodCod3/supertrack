import pdfplumber
import re

def extraer_informacion_ticket(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        texto = page.extract_text()
        lines = texto.split('\n')
        
        products = []
        total = None
        purchase_date = None

        # Expresión regular mejorada para capturar products, precios e importes
        product_pattern = re.compile(r'(\d+)\s+([\w\s]+)\s+([\d,]+\s*€?)\s*([\d,]+\s*€?)?')

        for line in lines:
            # Extraer la fecha
            if 'OP:' in line:
                purchase_date = re.search(r'\d{2}/\d{2}/\d{4}', line).group(0)
            
            # Buscar products y precios
            match = product_pattern.search(line)
            if match:
                quantity = match.group(1)
                product_name = match.group(2).strip()
                unit_price = match.group(3).replace(',', '.').replace('€', '').strip()
                total_price = match.group(4) if match.group(4) else unit_price
                total_price = total_price.replace(',', '.').replace('€', '').strip()
                
                products.append({
                    'quantity': quantity,
                    'name': product_name,
                    'unit_price': float(unit_price),
                    'total_price': float(total_price)
                })
            
            # Extraer el total final
            if 'TOTAL (€)' in line:
                total = float(line.split()[-1].replace(',', '.'))

        return {
            'purchase_date': purchase_date,
            'products': products,
            'total': total
        }
