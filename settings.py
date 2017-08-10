DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'lehar',
    'password': '',
    'database': 'risk-bot'
}
ITEM_PIPELINES = ['app.pipelines.DatabasePipeline']

