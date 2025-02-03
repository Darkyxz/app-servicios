import mercadopago
from mercadopago.config import RequestOptions
from config import Config

class MercadoPagoService:
    def __init__(self):
        # Configura las opciones de solicitud
        request_options = RequestOptions(
            integrator_id=Config.MERCADOPAGO_INTEGRATOR_ID,
            platform_id=Config.MERCADOPAGO_PLATFORM_ID
        )
        # Inicializa el SDK de MercadoPago con el token de acceso y las opciones
        self.sdk = mercadopago.SDK(Config.MERCADOPAGO_ACCESS_TOKEN, request_options=request_options)

    def create_preference(self, items):
        preference_data = {
            "items": items,
            "back_urls": {
                "success": "http://localhost:5000/payment/success",  # URL de éxito
                "failure": "http://localhost:5000/payment/failure",  # URL de fallo
                "pending": "http://localhost:5000/payment/pending"   # URL de pendiente
            },
            "auto_return": "approved",  # Redirige automáticamente al usuario después del pago
            "payment_methods": {
                "excluded_payment_types": [
                    {"id": "atm"}  # Excluye métodos de pago no deseados (opcional)
                ],
                "installments": 6  # Número máximo de cuotas permitidas
            }
        }
        preference_response = self.sdk.preference().create(preference_data)
        if 'response' in preference_response:
            return preference_response['response']['init_point']  # Devuelve la URL de pago
        else:
            raise Exception(f"Error creating preference: {preference_response}")