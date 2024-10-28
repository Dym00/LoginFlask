from flask import Flask, render_template, request

class MyFlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/login', 'login', self.login, methods=["GET", "POST"])

    def index(self):
        return render_template('index.html')

    def login(self):
         if request.method == 'POST':
             email = request.form['email']
             pwd = request.form['pwd']

             if not email or not pwd:
                return render_template('login.html')
            
         
         return render_template('login.html', error='Por favor, preencha todos os campos.')


    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    app = MyFlaskApp()
    app.run()       