from app import app

@app.route('/index')
def index():
    
    a=2
    b=4
    return str(a+b)

@app.route('/lol')
def lol():
    return'vikalp'
