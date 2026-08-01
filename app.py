from flask import Flask, render_template


app = Flask(__name__)

app.json.ensure_ascii = False

@app.route('/')
def home():
    page = "home"
    page_name = "მთავარი გვერდ"
    return render_template("index.html", page=page, page_name=page_name)

@app.route('/multiply/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
def multiply(num1, num2, num3, num4):
    page = "multiply"
    page_name = "გამრავლება"
    result = num1 * num2 * num3 * num4
    return render_template("index.html", page=page, page_name=page_name, result=result)

@app.route('/json')
def json():
    page = "json"
    page_name = "JSON მონაცემები"
    posts = [
        {"author":"გელა გელაშვილი", "title": "პირველი პოსტი", "content":"პირველი პოსტის შინაარსი", "date":"2024-01-16"},
        {"author":"გიორგი გიორგაძე", "title": "მეორე პოსტი", "content":"მეორე პოსტის შინაარსი", "date":"2025-12-06"},
        {"author":"ია იაძე", "title": "მესამე პოსტი", "content":"მესამე პოსტის შინაარსი", "date":"2024-03-25"},
        {"author":"თათია თათიაშვილი", "title": "მეოთხე პოსტი", "content":"მეოთხე პოსტის შინაარსი", "date":"2024-07-29"}
        ]
    
    return render_template('index.html', page=page, page_name=page_name, posts=posts)


@app.route('/user/<user_name>',methods = ['GET','POST'])
def user(user_name):
     page = "user"
     page_name = "მომხმარებლის გვერდი"
     return render_template('index.html', page=page, page_name=page_name, user_name=user_name)

@app.errorhandler(404)
def page_not_found(error):
    page = "error"
    page_name = "შეცდომა 404"
    return render_template('index.html', page=page, page_name=page_name)


if __name__ == '__main__':
    app.run(debug=True)