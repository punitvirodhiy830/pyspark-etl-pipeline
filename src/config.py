import os


INPUT_FILE = os.getenv(
    "INPUT_FILE",
    "data/orders.csv"
)

POSTGRES_URL = os.getenv(
    "POSTGRES_URL",
    "jdbc:postgresql://localhost:5432/ecommerce"
)

POSTGRES_USER = os.getenv(
    "POSTGRES_USER",
    "postgres"
)

POSTGRES_PASSWORD = os.getenv(
    "POSTGRES_PASSWORD"
)

TARGET_TABLE = os.getenv(
    "TARGET_TABLE",
    "orders"
)