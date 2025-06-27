# Superset configuration file
import os

# Database configuration - Force PostgreSQL
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://superset:superset@superset_postgres:5432/superset'

# Disable SQLite usage completely
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Thread safety configuration
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
    'echo': False
}

# Async query configuration - Disable problematic async features
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ALERT_REPORTS": False,
    "DASHBOARD_NATIVE_FILTERS": True,
}

# SQL Lab configuration
SQLLAB_ASYNC_TIME_LIMIT_SEC = 300
SQL_MAX_ROW = 10000

# Security
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY', 'mysecretkey')

# Disable Celery for SQL Lab (use synchronous execution)
class CeleryConfig:
    broker_url = 'memory://'
    result_backend = 'cache+memory://'
    task_always_eager = True
    task_eager_propagates = True

CELERY_CONFIG = CeleryConfig
