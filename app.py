from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    instructor = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)


@app.route('/')
def home():
    courses=Course.query.all()
    return render_template('index.html', courses=courses)


@app.route('/add', methods=['GET', 'POST'])
def add_course():

    if request.method == 'POST':

        title = request.form['title']
        instructor = request.form['instructor']
        description = request.form['description']

        course = Course(
            title=title,
            instructor=instructor,
            description=description
        )
        db.session.add(course)
        db.session.commit()

        return redirect('/')

    return render_template('add_course.html')


@app.route('/delete/<int:id>')
def delete(id):

    course = Course.query.filter_by(id=id).first()

    db.session.delete(course)
    db.session.commit()

    return redirect('/')
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    course = Course.query.filter_by(id=id).first()

    if request.method == 'POST':

        course.title = request.form['title']
        course.instructor = request.form['instructor']
        course.description = request.form['description']

        db.session.commit()

        return redirect('/')

    return render_template('update.html', course=course)


if __name__ == '__main__':
    app.run(debug=True, port=8000)