from DatabaseConnection import DatabaseConnection

def main():
    # Primera conexión
    db1 = DatabaseConnection()
    connection1 = db1.connect()

    # Segunda conexión
    db2 = DatabaseConnection()
    connection2 = db2.connect()

    # Verificar si ambas conexiones son iguales
    # ¿Qué diferencia hay entre que la instancia sea única y que la conexión también lo sea?
    print(f"¿Es la misma instancia? {db1 is db2}")
    print(f"¿Es la misma instancia? {connection1 is connection2}")

if __name__ == "__main__":
    main()

# ¿Qué evidencia en la salida muestra que la conexión solo se crea una vez?
# ¿Qué pasaría si eliminamos el patrón Singleton de la clase DatabaseConnection?