from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/')
def index():
	return render_template('index.html')


def main():
	app.run(port=8000, host='127.0.0.1')


if __name__ == '__main__':
	main()
