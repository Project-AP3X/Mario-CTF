import os

from flask import Flask

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import sys
from . import db
from . import api
from mario.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash
import functools
import base64


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'mysecretkey' # Set a secret key to enable sessions
    app.config.from_mapping(
        SECRET_KEY='nw-ctf-443-mario',
        #DATABASE=os.path.join(app.instance_path, 'mario.sqlite'),
        DATABASE='/home/admin/mario.sqlite',
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    # app.register_blueprint(api.bp)



    def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return redirect(url_for('auth.login'))

            return view(**kwargs)

        return wrapped_view

    @app.before_request
    def before_request():
        g.user = None
        if 'user_id' in session:
            g.user = session['user_id']

    @app.route('/')
    def homePage():
        before_request()
        if g.user:
            message = "net-sec{m@mA-M!a}"
            encoded_message = base64.b64encode(message.encode('utf-8')).decode('utf-8')
            return render_template('welcome_logged_in.html', message = encoded_message)
        else:
            return render_template('welcome.html')



    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            db = get_db()
            error = None
            user = db.execute(
                'SELECT * FROM user WHERE username = ?', (username,)
            ).fetchone()

            if user is None:
                error = 'Incorrect username.'
            elif user['password'] != password:
                error = 'Incorrect password.'

            if error is None:
                session.clear()
                session['user_id'] = user['id']
                g.user = user
                return redirect(url_for('challenge'))

            flash(error)

        return render_template('login.html')

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        return redirect(url_for('homePage'))

    @login_required
    @app.route('/challenge', methods=['GET', 'POST'])
    def challenge():
        before_request()
        if g.user:
            return render_template('challenge.html')
        else:
            return render_template('welcome.html')

    @app.after_request
    def add_security_headers(response):
        nonce = '3f31feefda72a6dbd0ced1b9eed3830c'
        response.headers['Content-Security-Policy'] = f"default-src 'self' *; script-src 'self' * 'nonce-{nonce}'; style-src 'self' * 'unsafe-inline'"
        response.headers['X-Content-Security-Policy'] = f"default-src 'self' *; script-src 'self' * 'nonce-{nonce}'; style-src 'self' * 'unsafe-inline'"
        response.headers['X-WebKit-CSP'] = f"default-src 'self' *; script-src 'self' * 'nonce-{nonce}'; style-src 'self' * 'unsafe-inline'"
        response.headers['nonce'] = nonce
        return response


    # Define the questions and answers for the quiz
    questions = [
        {
            "question": "Which of the Mario games came first?",
            "image": "/images/mario1.webp",
            "answers": [
                {"text": "Super Mario Odyssey", "correct": False},
                {"text": "Super Mario Run", "correct": False},
                {"text": "Mario Bros.", "correct": True},
                {"text": "New Super Mario Bros.", "correct": False}
            ]
        },
        {
            "question": "In which game did Mario first appear?",
            "image": "/images/mario2.webp",
            "answers": [
                {"text": "Ice Climber", "correct": False},
                {"text": "Donkey Kong", "correct": True},
                {"text": "The Legend of Zelda", "correct": False},
                {"text": "Kid Icarus", "correct": False}
            ]
        },
        {
            "question": "What was Mario's original name?",
            "image": "/images/mario3.webp",
            "answers": [
                {"text": "Spanner Dude", "correct": False},
                {"text": "Paolo", "correct": False},
                {"text": "Jumpman", "correct": True},
                {"text": "Fabio", "correct": False}
            ]
        },
        {
            "question": "What kind of job did he do before plumbing?",
            "image": "/images/mario4.webp",
            "answers": [
                {"text": "Baker", "correct": False},
                {"text": "Carpenter", "correct": True},
                {"text": "Dentist", "correct": False},
                {"text": "Poet", "correct": False}
            ]
        },
        {
            "question": "Bowser hasn't always been a villain. In which game was he one of the good guys?",
            "image": "/images/mario5.webp",
            "answers": [
                {"text": "Luigi's Mansion 3", "correct": False},
                {"text": "Super Mario RPG: Legend of the Seven Stars", "correct": True},
                {"text": "Mini Mario & Friends: Amiibo Challenge", "correct": False},
                {"text": "Mario and Donkey Kong: Minis on the move", "correct": False}
            ]
        },
        {
            "question": "In which year was the Super Mario Bros. film released? ",
            "image": "/images/mario6.webp",
            "answers": [
                {"text": "1993", "correct": True},
                {"text": "2001", "correct": False},
                {"text": "2007", "correct": False},
                {"text": "There has never been a Super Mario Bros. film, ever", "correct": False}
            ]
        },
        {
            "question": "What is the name of the level featured in every version of Super Mario Kart?",
            "image": "/images/mario7.webp",
            "answers": [
                {"text": "Apple Avenue", "correct": False},
                {"text": "Thunder Island", "correct": False},
                {"text": "Hiccup Highway", "correct": False},
                {"text": "Rainbow Road", "correct": True}
            ]
        },
        {
            "question": "Why do Mario and Luigi have moustaches?",
            "image": "/images/mario8.webp",
            "answers": [
                {"text": "Because they were born with them", "correct": False},
                {"text": "It was hard to give the characters facial expressions in early versions of the game", "correct": True},
                {"text": "Because they don't have razors", "correct": False},
                {"text": "Because it's fashionable", "correct": False}
            ]
        },
        {
            "question": "What was Princess Peach's name originally?",
            "image": "/images/mario9.webp",
            "answers": [
                {"text": "Princess Toadstool", "correct": True},
                {"text": "Princess Apple", "correct": False},
                {"text": "Princess Tangerine", "correct": False},
                {"text": "Princess Raisin", "correct": False}
            ]
        },
        {
            "question": "How does Mario smash bricks in the platform game?",
            "image": "/images/mario10.webp",
            "answers": [
                {"text": "With his forehead", "correct": False},
                {"text": "With a spanner", "correct": False},
                {"text": "With his hand", "correct": True},
                {"text": "With his moustache", "correct": False}
            ]
        }
    ]


    # Define the quiz page
    @app.route('/quiz', methods=['GET', 'POST'])
    def quiz():
        if request.method == 'POST':
            # If this is a form submission, process the answer and update the score
            answer = request.form['answer']
            question_index = int(request.form['question_index'])
            if questions[question_index]['answers'][int(answer)]['correct']:
                session['score'] = session.get('score', 0) + 1
            session['question_index'] = question_index + 1
        else:
            # If this is the first time visiting the quiz page, initialize the session variables
            session['score'] = 0
            session['question_index'] = 0

        # If all questions have been answered, redirect to the score page
        if session['question_index'] >= len(questions):
            return redirect(url_for('score'))

        # Otherwise, render the quiz page with the current question and answer choices
        current_question = questions[session['question_index']]
        return render_template('quiz.html', question=current_question, score=session['score'], questions=questions)


    # Define the score page
    @app.route('/score')
    def score():
        # Display the final score
        return render_template('score.html', score=session['score'], total=len(questions))


    @app.route('/verify', methods=['GET', 'POST'])
    def verify_flag():
        if request.method == 'POST':
            flag = request.form['flag']

            db = get_db()
            row = db.execute(
                'SELECT flag FROM flags WHERE flag=?', (flag,)
            ).fetchone()

            if row:
                if g.user:
                    # flag is valid
                    message = "Congratulations! The flag is valid. Since you got the admin privileges, I feel generous enough to give you a hint. Do you know about Stenography and images? Well there is an image on this page! Oops I said too much!"
                    return render_template('verify.html', message=message)
                else:
                    # flag is valid
                    message = "Congratulations! The flag is valid."
                    return render_template('verify.html', message=message)


                # # flag is valid
                # message = "Congratulations! The flag is valid."
                # return render_template('verify.html', message=message)
            else:
                # flag is invalid
                message = "Sorry, the flag is invalid. Please try again."
                return render_template('verify.html', message=message)
        else:
            return render_template('verify.html')


    return app