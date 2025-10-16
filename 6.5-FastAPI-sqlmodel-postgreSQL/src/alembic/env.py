import os
from logging.config import fileConfig
from urllib.parse import quote_plus

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Alembic Config object
config = context.config

# IMPORTANT: Use psycopg2 (synchronous) for Alembic, not asyncpg
# Change asyncpg to psycopg2

db_url = os.getenv("db_url")

# Escape '%' for ConfigParser safety
escaped_url = db_url.replace("%", "%%")

# Set the URL in Alembic config
config.set_main_option("sqlalchemy.url", escaped_url)

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import SQLModel metadata
from db.models import SQLModel
from sqlmodel import SQLModel as _SQLModel

# Let Alembic autogenerate migrations from SQLModel metadata
target_metadata = _SQLModel.metadata

# Optional: detect column type changes
compare_type = True


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


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()