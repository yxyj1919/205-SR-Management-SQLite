import os

class Config:
    DATABASE = os.getenv('FLASK_DATABASE', 'sr_management.db')
    DATABASE_DIR = os.getenv('FLASK_DATABASE_DIR', 'data')
    DATABASE_PATH = f'{DATABASE_DIR}/{DATABASE}' 