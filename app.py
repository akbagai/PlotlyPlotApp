from flask import Flask
from flask import Flask, render_template
import json
import plotly
from plotly.offline import init_notebook_mode, iplot
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from flask import Markup


app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to TutsPlus!"

#Once you have the JSON data, you'll pass it to the template file to be rendered
@app.route('/showLineChart')
def line():
	#using the numpy.linspace method to create evenly spaced samples calculated over the interval.
	#creates 500 evenly spaced samples between 0 and 100 for the x-axis scale.
	count = 500
	xScale = np.linspace(0, 100, count)

	#use numpy.random.randn to create random samples for the y-axis scale
	yScale = np.random.randn(count)

	#Create a trace using the plotly.graph_objs.scatter method
	trace = go.Scatter(
	    x = xScale,
	    y = yScale
	)

	#You need to convert the trace into JSON format. For that, you'll make use of the plotly JSON encoder plotly.utils.PlotlyJSONEncoder.
	data = [trace]
	graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

	#return render_template('index.html')
	return render_template('index.html',graphJSON=graphJSON)


@app.route('/showMultiChart')
def multiLine():
    count = 500
    xScale = np.linspace(0, 100, count)
    y0_scale = np.random.randn(count)
    y1_scale = np.random.randn(count)
    y2_scale = np.random.randn(count)
 
    # Create traces
    trace0 = go.Scatter(
        x = xScale,
        y = y0_scale
    )
    trace1 = go.Scatter(
        x = xScale,
        y = y1_scale
    )
    trace2 = go.Scatter(
        x = xScale,
        y = y2_scale
    )
    data = [trace0, trace1, trace2]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                           graphJSON=graphJSON)

def plot_test():
	months = ['Jan', 'Feb', 'Mar']
	user = [10,50,30]
	t20h = [17, 46, 39]

	#offline.init_notebook_mode()

	trace1 = go.Scatter(x= months, y=user, mode='lines+markers', name="OHR")
	trace2 = go.Scatter(x= months, y=t20h, mode='lines+markers', name="T20H")
	data = [trace1, trace2]

	#config={'showLink': False}
	config={'modeBarButtonsToRemove': ['sendDataToCloud'], 'displaylogo': False, 'showTips': False,'showLink': False }
	#config={'modeBarButtonsToRemove': ['sendDataToCloud', 'autoScale2d', 'resetScale2d'], 'displaylogo': False, 'showTips': False,'showLink': False }
	#config={'modeBarButtonsToRemove': ['sendDataToCloud']}
	#config = {'linkText': "Let's visit plot.ly !!!"}
	#iplot(data, config=config)
	#offline.iplot(data, show_link=False, config={'modeBarButtonsToRemove': ['sendDataToCloud']})

	layout = go.Layout(title='Test', xaxis=dict(title='Months'), yaxis=dict(title='Test'))
	fig = go.Figure(data=data, layout=layout)
	div_output = plotly.offline.plot(fig, output_type='div', include_plotlyjs=False, config=config)

	return div_output

@app.route('/offline')
def offline():

    plotly_graph = plot_test()
    return render_template("index1.html", plotly_graph=Markup(plotly_graph))