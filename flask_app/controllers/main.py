from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import User as u
from flask_app.models import List as l
from flask_app.models import Task as t
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:user_id>')
def dashboard(user_id):
    data = {'user_id': user_id}
    user = u.User.get_user_by_id(data)
    lists = l.List.get_all_lists_by_user(data)
    return render_template('dashboard.html', user=user, lists=lists)

@app.route('/<int:user_id>/<int:list_id>')
def list_detail(user_id, list_id):
    data = {
        'user_id': user_id,
        'list_id': list_id
    }
    list_detail = l.List.get_list_by_id(data)
    list_items = t.Task.get_tasks_by_list_id(data)
    return render_template('list_detail.html', list=list_detail, tasks=list_items)