from flask import Flask, render_template, request

from WebBanHang import data

app = Flask(__name__)


@app.route("/")
def index():
    cates = data.load_categories()

    keyWord = request.args.get("keyWord")
    prods = data.load_products(keyWord)


    return render_template('index.html', categories = cates, products = prods)


if __name__ == '__main__':
    app.run(debug=True)
