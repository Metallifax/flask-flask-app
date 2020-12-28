from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# Model Shape
class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  author = db.Column(db.String(20), nullable=False, default='Anonymous')
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return 'Blog post: ' + str(self.id)


all_posts = [
  {
    'title': 'Post 1',
    'content': 'Post 1 content here! Woweee!!!',
    'author': 'Aaron'
  },
  {
    'title': 'Post 2',
    'content': 'Post 2 content here! Omergerd!!!'
  },
]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/posts')
def posts():
  return render_template('posts.html', posts=all_posts)

@app.route('/onlyget', methods=['GET'])
def get_req():
  return 'You can only get this webpage.'

@app.route('/home/<string:name>')
def hello(name):
  return 'Hello, ' + name

if __name__ == "__main__":
  app.run(debug=True)
