# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__,static_folder="../static",template_folder='../templates')
import config.config as config


app.config.from_object(config) #通过配置对象来配置整个应用程序网站的配置

app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'