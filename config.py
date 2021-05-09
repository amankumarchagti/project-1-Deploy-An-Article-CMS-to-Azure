import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_APP= 'application.py'
    SECRET_KEY =  'secret-key'

    BLOB_ACCOUNT =  'project1storageaccount'
    BLOB_STORAGE_KEY =  'gkKXeqr9tiLSFTLk0jkZjv5Otjq/+ApSnTU+oZZt2WzbkGZWKoRuddRZlLHRnLWrnsT4LkiD4IiQhWcka/LXww=='
    BLOB_CONTAINER = 'project1-container'

    SQL_SERVER = 'project1-sql-server.database.windows.net'
    SQL_DATABASE = 'project1-database'
    SQL_USER_NAME = 'udacityadmin'
    SQL_PASSWORD =  'Udacity@2000'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "k-P3eqbn.jVT3o7bOag-oykR8px3UpD8~M"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "64181b4c-45b9-4876-97f7-da0d9a05aa3a"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
