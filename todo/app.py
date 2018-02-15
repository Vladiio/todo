from flask import Flask, render_template, request, redirect, url_for

from db import session
from todo.models import List, Item

app = Flask(__name__)


@app.route('/')
def home_view():
    return render_template('home.html')


@app.route('/create-list', methods=['POST'])
def create_list_view():
    list_ = List().save()
    item_content = request.form.get('item')
    Item(content=item_content, list=list_).save()
    return redirect(url_for('detail_list_view', list_id=list_.id))


@app.route('/lists/<int:list_id>/', methods=['POST', 'GET'])
def detail_list_view(list_id):
    list_ = session.query(List).filter(List.id==list_id).one()
    if request.method == 'POST':
        item_content = request.form.get('item')
        Item(content=item_content, list=list_).save()
    return render_template('list.html', list=list_)