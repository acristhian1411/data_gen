import random
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('ventas.sql', 'w') as file:

    # Define la cantidad de registros a generar para la tabla "ventas"
    num_registros_ventas = 50  # Puedes ajustar este número según tu necesidad

    # Genera datos para la tabla "ventas"
    for vent_id in range(1, num_registros_ventas + 1):
        cli_id = random.randint(1, 100)
        vend_id = random.randint(1, 100)
        vent_fecha = fake.date_between(start_date='-1y', end_date='today')

        insert_sql = f"INSERT INTO ventas (VENT_ID, CLI_ID, VEND_ID, VENT_FECHA) VALUES ({vent_id}, {cli_id}, {vend_id}, '{vent_fecha}');"
        file.write(insert_sql + '\n')

        # Genera al menos 5 detalles de venta por cada venta
        num_detalles_venta = random.randint(5, 10)  # Genera entre 5 y 10 detalles
        for _ in range(num_detalles_venta):
            prod_id = random.randint(1, 50)
            dven_cant = random.randint(1, 20)  # Puedes ajustar este rango según tu necesidad

            # Consulta SQL para obtener el precio del producto
            dven_precio_sql = f"select case when (select ct.TCLI_NAME from clientes c join cliente_tipos ct on ct.TCLI_ID = c.TCLI_ID where c.CLI_ID = {cli_id}) like '%mayorista%' then p.PROD_PMAYO else p.PROD_PMINO end precio from productos p where p.PROD_ID = {prod_id};"

            insert_sql = f"INSERT INTO venta_detalles (VENT_ID, PROD_ID, DVEN_CANT, DVEN_PRECIO, DEVEN_MIVA) VALUES ((SELECT VENT_ID FROM ventas WHERE VENT_ID = {vent_id}), {prod_id}, {dven_cant}, ({dven_precio_sql}), 10);"
            file.write(insert_sql + '\n')

print(f"Se han generado {num_registros_ventas} registros para la tabla 'ventas' con al menos 5 detalles cada una.")
