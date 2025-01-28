from flask import Flask, render_template
from meme import Meme

app = Flask(__name__)
meme = Meme()

@app.route('/')
def index():
    meme_pic, subreddit = meme.getMeme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host='0.0.0.0', port=80, debug=True)
