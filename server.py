from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html", tools=["diff_objects"])

@app.route('/diff_objects', methods=['POST', 'GET'])
def diff_objects():
   if request.method == "GET":
      return render_template("diff_objects.html", has_result=False)
   else:
      obj0 = eval(request.form['obj0'])
      obj1 = eval(request.form['obj1'])
      assert isinstance(obj0, set)
      assert isinstance(obj1, set)
      diff01 = "obj0 - obj1: %s" % (obj0 - obj1)
      diff10 = "obj1 - obj0: %s" % (obj1 - obj0)
      return render_template("diff_objects.html", has_result=True, diff01=diff01, diff10=diff10)

if __name__ == '__main__':
   app.run(debug=True)