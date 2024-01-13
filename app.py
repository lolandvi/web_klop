from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных,
        </header>
        
        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Клопенкова Виктория, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Клопенкова Виктория Владимировна, Лабораторная работа № 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа № 1
        </header>
        
        <h1>web-сервер на flask</h1>

        <main>
            <br>
            <div>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые ба-
                зовые возможности.
            </div>
            <br>
            <a href='/menu'>Назад к меню</a>

            <h2>Реализованные роуты</h2>
            <ul>
            <li><a href='/lab1/oak'>Дуб</a></li>
            <li><a href='/lab1/student'>Студенты</a></li>
            <li><a href='/lab1/python'>О Python</a></li>
            </ul>
        </main>

        <footer>
            &copy; Клопенкова Виктория, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''

@app.route('/lab1/oak') 
def oak():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''"
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''" width=600px, height=500px>
    </body>
</html>
'''

@app.route('/lab1/student')
def students():
    return '''
<!doctype html>
<html>
    <body>
        <main>
            <br>
            <div>
                Клопенкова Виктория Владимировна
            </div>
            <br>

            <h1>Логотип</h1>
            <img src="''' + url_for('static', filename='лого.jpg') + '''" width=500px, height=300px>
        </main>

        <footer>
            &copy; Клопенкова Виктория, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <body>
        <main>
            <br>
            <div>
                Python — это интерпретируемый, объектно-ориентированный язык программирования, который 
                известен своей чистотой и простотой в использовании. Он предоставляет широкие возможности 
                разработчикам благодаря своей читаемости и простоте синтаксиса. Python активно используется 
                во многих сферах, начиная от веб-разработки и научных исследований и заканчивая созданием игр, 
                анализом данных и разработкой искусственного интеллекта. Его гибкость и многофункциональность 
                делают его одним из самых популярных языков программирования в мире.
            </div>
            <br>
            <div>
                Одним из фундаментальных преимуществ Python является его богатая экосистема библиотек. 
                Библиотеки, такие как NumPy, Pandas, Matplotlib, TensorFlow и многие другие, делают Python 
                основным инструментом для научных исследований, обработки данных и машинного обучения. Кроме 
                того, наличие фреймворков веб-разработки, таких как Django и Flask, делают Python эффективным 
                выбором для создания веб-приложений и API. Большое количество библиотек делает Python незаменимым 
                инструментом для широкого круга разработок, включая робототехнику, игровую индустрию, научные 
                исследования и многое другое.
            </div>
            <br>
            <div>
                Python продолжает оставаться актуальным благодаря своей дружелюбной и поддерживающей разработчиков 
                атмосфере. Активное сообщество разработчиков постоянно обогащает его экосистему, добавляя новые 
                библиотеки и инструменты, что поддерживает его рост и популярность в современной разработке программного обеспечения.
            </div>
            <br>
            <img src="''' + url_for('static', filename='питон.jpg') + '''" width=500px, height=350px>
        </main>

        <footer>
            &copy; Клопенкова Виктория, ФБИ-11, 3 курс, 2023
        </footer>    
    </body>
</html>    
'''

@app.route('/proba', methods=['GET', 'POST'])
def proba():
    result = None
    if request.method == 'POST':
        first_value = request.form['first_value']
        second_value = request.form['second_value']
        if first_value and second_value:
            if first_value.isdigit():  # Проверяем, что первое значение является числом
                result = ' '.join([second_value for _ in range(int(first_value))])
            else:
                result = 'Первое значение должно быть числом!'
        else:
            result = 'Оба поля должны быть заполнены!'
    return render_template('input.html', result=result)

if __name__ == '__main__':
    app.run()
