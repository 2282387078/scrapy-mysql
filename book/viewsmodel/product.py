from flask import Blueprint,render_template,request,session
from models.book import Books

product = Blueprint('product',__name__,static_folder='static',template_folder='templates')


@product.route('/',methods=['get','post'])
def index():
    book_list = Books.query.all()
    return render_template('books.html',book_list = book_list)