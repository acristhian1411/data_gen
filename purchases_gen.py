import random
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('compras.sql', 'w') as file:

    # Define la cantidad de registros a generar para la tabla "compras"
    num_registros_compras = 50  # Puedes ajustar este número según tu necesidad

    # Genera datos para la tabla "compras"
    for comp_id in range(1, num_registros_compras + 1):
        prov_id = random.randint(1, 100)
        comp_fecha = fake.date_between(start_date='-1y', end_date='today')

        insert_sql = f"INSERT INTO compras (COMP_ID, PROV_ID, COMP_FECHA) VALUES ({comp_id}, {prov_id}, '{comp_fecha}');"
        file.write(insert_sql + '\n')

        # Genera al menos 5 detalles de compra por cada compra
        num_detalles_compra = random.randint(5, 10)  # Genera entre 5 y 10 detalles
        for _ in range(num_detalles_compra):
            prod_id = random.randint(1, 50)
            dcom_cant = random.randint(1, 20)  # Puedes ajustar este rango según tu necesidad

            # Consulta SQL para obtener el precio del producto
            dcom_precio_sql = f"SELECT PROD_PCOSTO FROM productos p WHERE p.PROD_ID = {prod_id};"

            insert_sql = f"INSERT INTO compras_det (COMP_ID, PROD_ID, DCOM_CANT, DCOM_PRECIO, DCOM_MIVA) VALUES ((SELECT COMP_ID FROM compras WHERE COMP_ID = {comp_id}), {prod_id}, {dcom_cant}, ({dcom_precio_sql}), 10);"
            file.write(insert_sql + '\n')

print(f"Se han generado {num_registros_compras} registros para la tabla 'compras' con al menos 5 detalles cada una.")
