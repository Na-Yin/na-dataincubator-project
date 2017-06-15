from flask import Flask, render_template, request, redirect
import api_pull as ap
import plot

app = Flask(__name__)

app.vars={}

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        #request was a post
        app.vars['ticker'] = request.form['ticker']
        app.vars['results'] = ap.get_data(app.vars['ticker'])
        script, div = plot.fig(app.vars['results'], app.vars['ticker'])
        f = open('%s.txt'%(app.vars['ticker']),'w')
        f.write('Ticker: %s\n'%(app.vars['ticker']))
        f.close()
        #return redirect('/results')
        return render_template('results.html', script=script, div=div)

# Add else: for error handling; render_template with message for if ticker does not result in data; change ^else: to elif based on request resulting in data

if __name__ == "__main__":
    app.run(debug=True)
