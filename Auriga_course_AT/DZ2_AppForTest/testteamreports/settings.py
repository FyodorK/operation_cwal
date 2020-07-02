APP_HOST = 'localhost'
APP_PORT = 5000
CERTIFICATE_FILE = __import__('os').path.join('certificate', 'cert.pem')
CERTIFICATE_KEY_FILE = __import__('os').path.join('certificate', 'key.pem')

# Only file name; file location is always in <product>/data folder
DATABASE_FILE = 'testteamreports.db'
REPORT_STORAGE_FOLDER = 'report_storage'

ADMIN_LOGIN = 'admin'
ADMIN_FACTORY_PASSWORD = 'admin'
