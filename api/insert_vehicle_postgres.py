import os
import time
import argparse
import pandas as pd
import numpy as np
from faker import Faker
from sqlalchemy import create_engine
from datetime import datetime
from dotenv import load_dotenv
from faker_vehicle import VehicleProvider

load_dotenv()

username = os.environ.get("POSTGRES_DATABASE_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("POSTGRES_PORT")
database = os.environ.get("POSTGRES_DATABASE")
table = os.environ.get("POSTGRES_TABLE")

# função para parsear a saída do parâmetro SILENT
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# Instancia a classe Faker
faker = Faker()
faker.add_provider(VehicleProvider)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate fake data...')

    parser.add_argument('--interval', type=int, default=0.005,
                        help='interval of generating fake data in seconds')
    parser.add_argument('-n', type=int, default=1,
                        help='sample size')
    parser.add_argument('--connection-string', '-cs', dest="connection_string", 
                        type=str, default=f'postgresql://{username}:{password}@{host}:{port}/{database}',
                        help='Connection string to the database')
    parser.add_argument('--silent', type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print fake data")

    args = parser.parse_args()

    print(f"Args parsed:")
    print(f"Interval: {args.interval}")
    print(f"Sample size; {args.n}")
    print(f"Connection string: {args.connection_string}", end='\n\n')

    #-----------------------------------------------------------------

    engine = create_engine(args.connection_string)

    print("Iniciando a simulacao...", end="\n\n")

    # Gera dados fake a faz ingestão
    while True:
        customer_id   = [faker.random_int() for i in range(args.n)]
        ano_modelo        = [faker.vehicle_year_make_model() for i in range(args.n)]
        modelo             = [faker.vehicle_make_model() for i in range(args.n)]
        fabricante             = [faker.vehicle_make() for i in range(args.n)]
        ano_veiculo     = [faker.vehicle_year() for i in range(args.n)]
        categoria  = [faker.vehicle_category() for i in range(args.n)]
        dt_update         = [datetime.now() for i in range(args.n)]

        df = pd.DataFrame({
            "customer_id": customer_id,
            "ano_modelo": ano_modelo,
            "modelo": modelo,
            "fabricante": fabricante,
            "ano_veiculo": ano_veiculo,
            "categoria": categoria,
            "dt_update": dt_update,
        })

        df.to_sql("vehicle", con=engine, if_exists="append", index=False)

        if not args.silent:
            print(df, end="\n\n")

        time.sleep(args.interval)