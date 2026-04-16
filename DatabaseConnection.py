import psycopg2
from psycopg2 import OperationalError

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # ¿Qué problema ocurre si esta clase se instancia múltiples veces?
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
            cls._instance._connection = None
        return cls._instance

    def connect(self):
        if not self._connection:
            try:
                # ¿Por qué la conexión no se crea cada vez que se llama la clase?
                self._connection = psycopg2.connect(
                    host="212.85.2.90",
                    port=5433,
                    database="clase_db",
                    user="xxxx",
                    password="xxxx"
                )
                print("Connection created.")
            except OperationalError as e:
                print(f"Error: {e}")
        return self._connection

# ¿Dónde se está controlando que solo exista una instancia?
# ¿Qué pasaría si eliminamos esta validación?