from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/play')                           
def level1():
    return render_template('level1.html')  

@app.route('/play/<int:num>')
def level2(num):
    num= num
    return render_template('level2.html', num=num)

@app.route('/play/<int:num>/<color>')
def level3(num,color):
    color_change= color
    return render_template('level3.html', num=num, color_change=color)


if __name__=="__main__":
    app.run(debug=True)                