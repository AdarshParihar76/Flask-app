import os


class Config:
    SECRET_KEY = '073bdf4763bca17a5ff041'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'adarshsparihar01@gmail.com'
    MAIL_PASSWORD = 'HelloA@76im'