from flask import Flask, render_template, request, redirect, session
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv('SECRET_KEY')