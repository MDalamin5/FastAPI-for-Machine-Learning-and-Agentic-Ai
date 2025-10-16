import os
from logging.config import fileConfig
from urllib.parse import quote_plus  # for password safety

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Alembic Config object gives access to values within alembic.ini
config = context.config

# ---- STEP 1: Build a safe PostgreSQL URL manually ----
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "temp_alembic")

# Encode password for URL safety
encoded_password = quote_plus(DB_PASSWORD)

# Construct full database URL
db_url = f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Escape '%' for ConfigParser safety
escaped_url = db_url.replace("%", "%%")

# Set the URL in Alembic config
config.set_main_option("sqlalchemy.url", escaped_url)

# ---- STEP 2: Setup logging ----
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ---- STEP 3: Import SQLModel metadata ----
from app.models import SQLModel  # Import your models
from sqlmodel import SQLModel as _SQLModel

# Let Alembic autogenerate migrations from SQLModel metadata
target_metadata = _SQLModel.metadata

# Optional: detect column type changes
compare_type = True


# ---- STEP 4: Migration runners ----
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=compare_type,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=compare_type,
        )

        with context.begin_transaction():
            context.run_migrations()


# ---- STEP 5: Entry point ----
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
