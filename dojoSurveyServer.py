from flask import Flask, render_template, request, redirect, flash
import os
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result',methods=['POST'])
def postResult():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(name) < 1 and len(comment) < 1:
        flash("Name cannot be empty")
        flash("Comment cannot be empty")
        return redirect('/')
    elif len(name) < 1:
        flash("Name cannot be empty")
        return redirect('/')
    elif len(comment) < 1:
        flash("Comment cannot be empty")
        return redirect('/')
    else:
        return render_template('result.html',name=name,location=location,language=language,comment=comment)
app.run(debug=True)
