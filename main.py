from textblob import TextBlob, translate
from flask import Flask, request

app = Flask(__name__)

@app.route('/translate')
def translate():
    text = request.args.get('t', default=".", type=str)
    blob = TextBlob(text)
    o_lang = blob.detect_language()
    print(o_lang)
    if o_lang == 'en':
        translation = blob.translate(to='pt')
    else:
        translation = blob.translate(to='en')
    return str(translation)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)