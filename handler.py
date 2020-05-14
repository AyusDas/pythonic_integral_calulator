from flask import Flask ,render_template, request
from pytexit import py2tex
from sympy import integrate
from sympy.abc import x
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    errors = []
    results = None
    if request.method == "POST":
        try:
            exp = request.form['data']
            results = py2tex(str(integrate(exp, x)))
        except:
            errors.append("Unable to reach client")
            print(errors)
    return render_template('index.html', errors=errors, results=results)

if __name__=='__main__':
    app.run(debug=True)
