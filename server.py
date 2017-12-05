from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def all():
    return render_template('all.html')

@app.route('/ninja/<color>')
def single(color):
    if color == 'blue':
        name = 'Leonardo'
        img_str = 'leonardo.jpg'
    elif color == 'purple':
        name = 'Donatello'
        img_str = 'donatello.jpg'
    elif color == 'red':
        name = 'Raphael'
        img_str = 'raphael.jpg'
    elif color == 'orange':
        name = 'Michelangelo'
        img_str = 'michelangelo.jpg'
    else:
        name = 'Who cares?'
        img_str = 'april.jpg'

    return render_template('single.html',link = img_str, color = color, name = name)


app.run(debug=True)