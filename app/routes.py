from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import User, Vote
from app import db

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/register')
def register():
    # Registration logic goes here
    return render_template('register.html')

@bp.route('/vote')
def vote():
    # Voting logic goes here
    return render_template('vote.html')
