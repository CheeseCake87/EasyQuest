import configparser

from flask import Flask
from flask_bigapp import BigApp, Auth
from flask_sqlalchemy import SQLAlchemy

bigapp = BigApp()
db = SQLAlchemy()
sysconf = configparser.ConfigParser()
auth = Auth()

__all__ = ["Flask", "bigapp", "db", "sysconf", "auth"]
