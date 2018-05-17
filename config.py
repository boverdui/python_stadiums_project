import os

project_dir = os.path.dirname(os.path.abspath(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(project_dir, "stadiumdatabase.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
