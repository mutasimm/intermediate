from flask import Flask, request, render_template, send_from_directory
import datetime

app = Flask(__name__)


#to serve the damn front cover image
@app.route('/image')
def image():
    return send_from_directory('static', 'main.jpg')

# concurrency testing part - necessary
@app.route('/delay')
def delay():
    currentDT = datetime.datetime.now()
    i = 0
    for j in range(50000000):
        i += j
    currentDT2 = datetime.datetime.now()
    return str(currentDT)[14:23] + "\n" + str(currentDT2)[14:23]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view_preface')
def view_preface():
    return render_template("preface.html")

@app.route('/view_contents')
def view_contents():
    return render_template("contents.html")

@app.route('/view_chapter_1')
def view_chapter_1():
    return render_template("chapter_1.html")

@app.route('/view_chapter_2')
def view_chapter_2():
    return render_template("chapter_2.html")

@app.route('/view_chapter_3')
def view_chapter_3():
    return render_template("chapter_3.html")

@app.route('/view_chapter_4')
def view_chapter_4():
    return render_template("chapter_4.html")

@app.route('/view_chapter_5')
def view_chapter_5():
    return render_template("chapter_5.html")

@app.route('/view_chapter_6')
def view_chapter_6():
    return render_template("chapter_6.html")

@app.route('/view_chapter_7')
def view_chapter_7():
    return render_template("chapter_7.html")

@app.route('/view_chapter_8')
def view_chapter_8():
    return render_template("chapter_8.html")

@app.route('/view_chapter_9')
def view_chapter_9():
    return render_template("chapter_9.html")

@app.route('/view_chapter_10')
def view_chapter_10():
    return render_template("chapter_10.html")

@app.route('/view_chapter_10_8')
def view_chapter_10_8():
    return render_template("chapter_10_8.html")

@app.route('/view_chapter_11')
def view_chapter_11():
    return render_template("chapter_11.html")

@app.route('/view_chapter_c1')
def view_chapter_c1():
    return render_template("chapter_c1.html")

@app.route('/view_chapter_appendix')
def view_chapter_appendix():
    return render_template("appedix.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
