from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/second')
def second():
    return "This is the second page"

@app.route('/third/subthird')
def third():
    return "This is the subpage of the third page"

@app.route('/dynamic/<int:id>')
def dynamic(id):
    return f"ID of this page is {id}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=30000)
