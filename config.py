import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Otras configuraciones (opcional)
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'false'
     # Configuración de Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'una_clave_secreta_por_defecto')  # Usa una clave por defecto si no está en .env
    # Configuración de MercadoPago
    MERCADOPAGO_ACCESS_TOKEN = os.getenv('MERCADOPAGO_ACCESS_TOKEN')
    MERCADOPAGO_PUBLIC_KEY = os.getenv('MERCADOPAGO_PUBLIC_KEY')
    MERCADOPAGO_INTEGRATOR_ID = os.getenv('MERCADOPAGO_INTEGRATOR_ID')
    MERCADOPAGO_PLATFORM_ID = os.getenv('MERCADOPAGO_PLATFORM_ID')

    # Configuración de Sanity
    SANITY_PROJECT_ID = os.getenv('SANITY_PROJECT_ID')
    SANITY_DATASET = os.getenv('SANITY_DATASET')
    SANITY_TOKEN = os.getenv('SANITY_TOKEN')
    
