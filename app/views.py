from flask import Flask, render_template, flash, redirect, session, url_for, request, g
from app import app, db, admin
from flask_admin.contrib.sqla import ModelView
from app.models import Todo
from .forms import TodoForm
admin.add_view(ModelView(Todo, db.session))
import time

# Index Page #
@app.route('/')
def home():
    return render_template("home.html")
# Incompleted tasks #
@app.route('/tasks')
def tasks():
    incomplete = Todo.query.filter_by(complete=False).all()
    return render_template('tasks.html', incomplete=incomplete)

# Completed tasks #
@app.route('/complete')
def complete_tasks():
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('complete_tasks.html', complete=complete)

# Creating and validating a task #
@app.route('/create_task', methods=['GET','POST'])
def create_task():
    form = TodoForm()
    todaysdate = time.strftime("%d/%m/%Y")
    if form.validate_on_submit():
        todo = Todo(title=form.title.data,description=form.description.data, complete=False, date=todaysdate)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('create_task.html', form = form)

# Mark a task as complete #
@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('tasks'))

# Delete a task from the database #
@app.route('/delete/<id>', methods=['GET'])
def delete_task(id):
    task = Todo.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('complete_tasks'))
