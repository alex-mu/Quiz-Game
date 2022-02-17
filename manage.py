from flask import Flask, render_template, request
    
    
app = Flask(__name__)
    
    
@app.route("/", methods=['GET', 'POST'])
def index():
        print(request.method)
        if request.method == 'POST':
            if request.form.get('Correct') == 'Correct':
                # pass
                print("Correct")
            elif  request.form.get('Wrong') == 'Wrong':
                # pass # do something else
                print("Wrong")
            else:
                # pass # unknown
                return render_template("index.html")
        elif request.method == 'GET':
            # return render_template("index.html")
            print("Try again")
        return render_template("index.html")
    
    
if __name__ == '__main__':
        app.run()