from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
app = Flask(__name__)       
proxied = FlaskBehindProxy(app)             

app.config['SECRET_KEY'] = '3af78194d11f5f973dd0c3f82a7be527'


@app.route("/")   
@app.route("/home")
def home():
  return render_template('home.html', subtitle='Home Page', text="Welcome to the home page")      
  
@app.route("/about")
def about():
  return render_template('about.html', subtitle="About", text="This is a second page")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':               
  app.run(debug=True, host="0.0.0.0")