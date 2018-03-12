#! /usr/bin/env python3

from color_control.rgb import start as rgb_start
from color_control.rgb import set_color
from flask import Flask, render_template, request

STARTING_COLOR = "#000000"

rgb_start()
set_color(STARTING_COLOR)
app = Flask(__name__)

@app.route('/')
def idx():
    return render_template('index.html', current_color=STARTING_COLOR)

@app.route('/recolor', methods=['POST'])
def recolor():
    color = request.form["rgb-color"]
    set_color(color)
    return render_template('index.html', current_color=color)

