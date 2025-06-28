
import json
from docx import Document
from datetime import datetime

def cargar_datos():
    try:
        with open("datos_prestamo.json", encoding="utf-8") as f:
            datos = json.load(f)
            print("✅ Datos cargados desde 'datos_prestamo.json'")
            return datos
    except FileNotFoundError:
        print("⚠️ Archivo 'datos_prestamo.json' no encontrado. Ingresar datos manualmente.")
        return pedir_datos_por_consola()

def pedir_datos_por_consola():
    print("📝 Ingrese los datos del contrato de mutuo:\n")
    return {
        "FECHA": input("Fecha (ej: 28 de junio de 2025): "),
        "NOMBRE_PRESTAMISTA": input("Nombre del prestamista: "),
        "RUT_PRESTAMISTA": input("RUT del prestamista: "),
        "DIRECCION_PRESTAMISTA": input("Dirección del prestamista: "),
        "NOMBRE_REPRESENTANTE": input("Nombre del representante legal: "),
        "NOMBRE_EMPRESA": input("Nombre de la empresa: "),
        "RUT_EMPRESA": input("RUT de la empresa: "),
        "DIRECCION_EMPRESA": input("Dirección de la empresa: "),
        "MONTO": input("Monto del préstamo (ej: $10.000.000): "),
        "PLAZO": input("Plazo del préstamo (ej: 12 meses): "),
        "FECHA_VENCIMIENTO": input("Fecha de vencimiento (ej: 28 de junio de 2026): "),
        "FORMA_PAGO": input("Forma de pago (ej: transferencia electrónica): "),
        "BANCO": input("Banco: "),
        "TIPO_CUENTA": input("Tipo de cuenta: "),
        "NUMERO_CUENTA": input("Número de cuenta: "),
        "INTERES": input("¿Devenga intereses? (ej: no devengará intereses): "),
        "INTERES_MORA": input("Interés por mora (ej: 2%): ")
    }

def reemplazar_variables(doc, datos):
    for p in doc.paragraphs:
        for key, value in datos.items():
            if f"{{{{{key}}}}}" in p.text:
                p.text = p.text.replace(f"{{{{{key}}}}}", value)

def generar_contrato():
    datos = cargar_datos()
    plantilla = "Contrato_Plantilla.docx"
    documento = Document(plantilla)

    reemplazar_variables(documento, datos)

    nombre_archivo = f"Contrato_Mutuo_{datos['NOMBRE_EMPRESA'].replace(' ', '_')}.docx"
    documento.save(nombre_archivo)
    print(f"✅ Contrato generado correctamente: {nombre_archivo}")

if __name__ == "__main__":
    generar_contrato()
