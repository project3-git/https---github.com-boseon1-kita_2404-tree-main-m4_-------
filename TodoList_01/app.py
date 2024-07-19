from flask import Flask, render_template, redirect, url_for, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# config파일을 만들었을 때 설정
# app.config.from_pyfile('config.py')
# app.config['SECRET_KEY'] = 'your_secret_key_here'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['SECRET_KEY'] = 'f249abac8a9020d2d79dadf2cea3e8294fbb60c83bff6282'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 테이블 - 테이블명 : Task , 컬럼 : id, content
class Task(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()]) # label태그의 for 속성값 == input태그의 name의 value값
    submit = SubmitField('Add Task')

# 방식은 GET, POST 두가지 방식 존재  
@app.route('/', methods=['GET', 'POST']) # 여기서는 두가지 방식을 다 허용
def index():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


# methods 선언이 안되어 있어서 기본값인 get 방식
@app.route('/tasks')
def tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'title':task.title} for task in tasks])


@app.route("/edit/<int:task_id>", methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get_or_404(task_id) # task_id가 없으면 404 에러를 발생시킴
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        db.session.commit()
        return redirect(url_for('index'))
    form.title.data = task.title
    return render_template('edit_task.html', form=form, task_id=task_id, task_title=task.title)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
        

if __name__ == '__main__' :
    with app.app_context():
        db.create_all()
    app.run(debug=True)