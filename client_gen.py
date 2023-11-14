import random
import faker
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('clientes.sql', 'w') as file:

    # Define la cantidad de registros a generar
    num_registros = 100
    #inserta tipos de clientes
    insert_sql = "INSERT INTO cliente_tipos (TCLI_ID, TCLI_NAME, TCLI_PSAGRE) VALUES(1, 'Mayorista', 15.0);"
    file.write(insert_sql + '\n')
    insert_sql = "INSERT INTO cliente_tipos (TCLI_ID, TCLI_NAME, TCLI_PSAGRE) VALUES(2, 'Minorista', 35.0);"
    file.write(insert_sql + '\n')

    for i in range(1,num_registros):
        # Genera datos aleatorios
        cli_id = i
        tcli_id = random.randint(1, 2)
        cli_apellido = fake.last_name()
        cli_nombre = fake.first_name()
        ruc_numero = fake.random_int(min=1000000, max=9999999)
        ruc_digito = random.randint(1, 9)
        cli_ruc = f'{ruc_numero}-{ruc_digito}'
        cli_dir = fake.street_address()
        cli_mail = fake.email()
        prov_telefono = fake.phone_number()
        max_length = 50  # Define la longitud máxima de la observación
        cli_obs = fake.text(max_nb_chars=max_length) if random.choice([True, False]) else None

        # Genera la sentencia SQL INSERT
        insert_sql = f"INSERT INTO clientes (CLI_ID,TCLI_ID, CLI_APELLIDO, CLI_NOMBRE, CLI_RUC, CLI_DIR, CLI_MAIL, PROV_TELEFONO_, CLI_OBS) VALUES ({cli_id}, {tcli_id}, '{cli_apellido}', '{cli_nombre}', '{cli_ruc}', '{cli_dir}', '{cli_mail}', '{prov_telefono}', '{cli_obs}');"

        # Escribe la sentencia SQL en el archivo
        file.write(insert_sql + '\n')

print(f"Se han generado {num_registros} registros y se han guardado en 'clientes.sql'.")
