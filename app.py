from flask import Flask, render_template

app = Flask(__name__)

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
