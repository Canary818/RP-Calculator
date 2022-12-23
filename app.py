from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/grades", methods = ["POST"])
def grades():
    global sub1
    global sub2
    global sub3
    global math
    global mathlevel

    sub1 = request.form.getlist("sub1")
    sub2 = request.form.getlist("sub2")
    sub3 = request.form.getlist("sub3")
    mathlevel = request.form.get("mathlevel")
    math = ["Math", mathlevel]

    return render_template("grades.html", sub1 = sub1, sub2 = sub2, sub3 = sub3, mathlevel = mathlevel)

@app.route("/result", methods = ["POST"])
def result():
    sub1grade = request.form.get("sub1grade")
    sub2grade = request.form.get("sub2grade")
    sub3grade = request.form.get("sub3grade")
    mathgrade =  request.form.get("mathgrade")
    gpgrade = request.form.get("gpgrade")

    sub1.append(int(sub1grade))
    sub2.append(int(sub2grade))
    sub3.append(int(sub3grade))
    math.append(int(mathgrade))

    subjectlist = [sub1, sub2, sub3, math]
    gradelist = []
   
    rp = 0

    H1 = False

    for i in range(4):
        if subjectlist[i][1] == "H1":
            gradelist.insert(0, subjectlist[i][2])
            H1 = True

        else:
            gradelist.append(subjectlist[i][2])

    if not H1:
        gradelist = sorted(gradelist)

    rp += calc_score(gradelist[0]) / 2
    rp += calc_score(int(gpgrade)) / 2

    for j in range(1, 4):
        rp += calc_score(gradelist[j])

    return render_template("result.html", rp = rp)


def calc_score(score):
    if score >= 70:
        return 20

    elif 70 > score >= 60:
        return 17.5

    elif 60 > score >= 55:
        return 15

    elif 55 > score >= 50:
        return 12.5

    elif 50 > score >= 45:
        return 10

    elif 45 > score >= 35:
        return 5

    elif score < 35:
        return 0

    return