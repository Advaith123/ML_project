from flask import Flask, render_template, request
import diet_recommender as dr
app = Flask(__name__)

@app.route('/')
def index():
    title = 'Diet Recommendation System'
    return render_template('index.html', title = title)


@app.route('/results', methods = ["POST"])
def results():
    title = 'Diet Recommendation System'
    age = request.form.get("age")
    veg = request.form.get("veg")
    weight = request.form.get("weight")
    height = request.form.get("height")
    func = request.form.get('func')
    print(age)
    print(veg)
    print(weight)
    print(height)
    if func == 'wloss':
        l = dr.Weight_Loss(int(age), int(veg), float(weight), float(height))
        print(l)
    elif func == 'wgain':
        l = dr.Weight_Gain(int(age), int(veg), float(weight), float(height))
        print(l)
    elif func == 'main':
        l = dr.Healthy(int(age), int(veg), float(weight), float(height))
        print(l)
    else:
        print(func)
    return render_template("results.html", title = title)

if __name__ == '__main__':
    app.run(debug=True)

