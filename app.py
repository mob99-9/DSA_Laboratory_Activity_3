from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def area_circle():
    result = None
    if request.method == 'POST':
        circle_radius = request.form.get('circle_radius', '')
        result = 3.14*float(circle_radius)**2
    return render_template('area_circle.html', result=result)

@app.route('/areaOftriangle', methods=['GET', 'POST'])
def area_triangle():
    result = None
    if request.method == 'POST':
        triangle_height = float(request.form.get('triangle_height', ''))
        triangle_base = float(request.form.get('triangle_base', ''))
        result = (triangle_height*triangle_base)/2
    return render_template('area_triangle.html', result=result)

@app.route('/infixpostfix', methods=['GET', 'POST'])
def infix_to_postfix():
    result = None
    if request.method == 'POST':
        import stack_shunting_yard_algo
        algo = stack_shunting_yard_algo
        user_infix = request.form.get('user_infix', '')
        result = algo.infix_to_postfix(user_infix)
    return render_template('infix_postfix.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
