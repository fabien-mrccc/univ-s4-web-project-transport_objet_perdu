from flask import Flask, session, request, redirect, render_template
import data_model as model

app = Flask(__name__)
