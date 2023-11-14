import random
import faker
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('proveedores.sql', 'w') as file:
    num_registros_presentacion = 4

    # Define la cantidad de registros a generar para la tabla "producto_tipos"
    num_registros_tipos = 4
    # Define la cantidad de registros a generar para la tabla "producto_tipos"
    num_registros_marcas = 10
    # Define la cantidad de registros a generar para la tabla "producto_origen"
    num_registros_origen = 3

    # Define la cantidad de registros a generar para la tabla "productos"
    num_registros_productos = 50  # Puedes ajustar este número según tu necesidad

     # Genera datos para la tabla "producto_presentacion"
    for i in range(1,num_registros_marcas):
        marca_id = i
        marca_desc = fake.word()
        insert_sql = f"INSERT INTO marcas (marca_id, marca_desc) VALUES ({marca_id},'{marca_desc}');"
        file.write(insert_sql + '\n')

     # Genera datos para la tabla "producto_presentacion"
    for i in range(1,num_registros_presentacion):
        preprod_id = i
        preprod_name = fake.unique.random_element(elements=('Botella vidrio', 'Lata', 'Botella plastico'))
        insert_sql = f"INSERT INTO producto_presentacion (PREPROD_ID, PREPROD_NAME) VALUES ({preprod_id},'{preprod_name}');"
        file.write(insert_sql + '\n')

    # Genera datos para la tabla "producto_tipos"
    for i in range(1,num_registros_tipos):
        tprod_id = i
        tprod_name = fake.unique.random_element(elements=('Gaseosas', 'Cervezas', 'Agua'))
        insert_sql = f"INSERT INTO producto_tipos (TPROD_ID,TPROD_NAME) VALUES ({tprod_id},'{tprod_name}');"
        file.write(insert_sql + '\n')

    # Genera datos para la tabla "producto_origen"
    for i in range(1,num_registros_origen):
        oprod_id = i
        oprod_name = fake.unique.random_element(elements=('Nacional', 'importada'))
        insert_sql = f"INSERT INTO producto_origen (OPROD_NAME) VALUES ({oprod_id},'{oprod_name}');"
        file.write(insert_sql + '\n')

    # Genera datos para la tabla "productos"
    for i in range(1,num_registros_productos):
        prod_id = i
        tprod_id = random.randint(1, (num_registros_tipos-1))
        marca_id = random.randint(1, (num_registros_marcas-1))
        oprod_id = random.randint(1, (num_registros_origen-1))
        preprod_id = random.randint(1, (num_registros_presentacion-1))
        prod_desc = fake.word()
        prod_pcosto = round(random.uniform(3500, 350000), 2)
        prod_pmayo = round(prod_pcosto * 1.15, 2)
        prod_pmino = round(prod_pcosto * 1.35, 2)
        prod_cant = random.randint(0, 200)

        insert_sql = f"INSERT INTO productos (PROD_ID,marca_id,TPROD_ID, OPROD_ID, PREPROD_ID, PROD_DESC, PROD_PCOSTO, PROD_PMAYO, PROD_PMINO, PROD_CANT) VALUES ({prod_id},{marca_id},{tprod_id}, {oprod_id}, {preprod_id}, '{prod_desc}', {prod_pcosto}, {prod_pmayo}, {prod_pmino}, {prod_cant});"
        file.write(insert_sql + '\n')