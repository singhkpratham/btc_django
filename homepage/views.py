from django.shortcuts import render, HttpResponse
from .models import Investment, HistData
import time
from threading import Thread
from urllib import request as req
import json
from datetime import datetime
import plotly.offline as opy
import plotly.graph_objs as go
import sqlite3
import pandas as pd
# Create your views here.
url = 'https://www.bitstamp.net/api/v2/ticker/btcusd/'
def home(request):
    x = [-2, 0, 4, 6, 7]
    y = [q ** 2 - q + 3 for q in x]
    con = sqlite3.connect("db.sqlite3")
    dat = (pd.read_sql_query("select * from homepage_histdata", con))
    trace1 = go.Scatter(x=dat.time, y=dat.rate, marker={'color': 'red', 'symbol': 104, 'size': "10"},
                        mode="lines", name='1st Trace')

    data = go.Data([trace1])
    layout = go.Layout(title="Meine Daten", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
    figure = go.Figure(data=data, layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    return render(request, "home.html", {'graph': div})

def sync(request):
    a = HistData()
    a.rate = json.loads(req.urlopen(url).read())['last']
    a.time = datetime.now()
    a.currency = 'USD'
    print(a)
    a.save()
    return HttpResponse("synced")

def this():
    pass
    # for i in range(10):
    #     print(i)
    #     b = Dummy()
    #     b.name = str(i)
    #     b.grade = i
    #     b.save()
    #     time.sleep(30)

# th = Thread(target=this)
# th.daemon = True
# th.start()
