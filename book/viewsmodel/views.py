from flask import request,render_template,redirect,session,abort
from config.app import app
from config.config import *
import hashlib
from models.model import *
from viewsmodel.product import product
#将admin蓝图注册进app
app.register_blueprint(product,url_prefix='/product')


# @app.before_request
# def breq():
#     print(request.args['username'])
#     if False:
#         return abort(501)

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def err404(error):
    return '404页面'

@app.errorhandler(400)
def err400(error):
    return '400页面'

@app.errorhandler(501)
def err501(error):
    return '501页面'