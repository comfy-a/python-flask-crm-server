#!/usr/bin/env python3

import connexion
from flask import Flask
from crm import encoder
from flask_cors import CORS, cross_origin
from crm.database_config import DatabaseConfig, mysql
import logging

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')

    DatabaseConfig(app.app)

    logger=logging.getLogger('main')
    app.add_api('swagger.yaml', arguments={'title': 'CRM'})
    app.app.json_encoder = encoder.JSONEncoder    
    CORS(app.app)

    app.run(port=8080)

if __name__ == '__main__':
    main()
