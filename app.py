from flask import Flask, request, render_template
from stories import story
app = Flask(__name__)

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        answers = {
            "place": request.form['place'],
            "noun": request.form['noun'],
            "verb": request.form['verb'],
            "adjective": request.form['adjective'],
            "plural_noun": request.form['plural_noun']
        }
        generated_text = story.generate(answers)
        return render_template('home.html', generated_text=generated_text)
    return render_template('home.html')

if __name__ == '__main__':
    app.run()