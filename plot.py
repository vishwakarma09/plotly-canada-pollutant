import plotly.graph_objects as go

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="weather"
)

def fetchArrayFromSql(sql):
	global mydb
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	return mycursor.fetchall()

#sql = """SELECT a.date, ifnull(a.average,0) as data1, ifnull(b.average,0) as data2, ifnull(c.average,0) as data3, ifnull(d.average,0) as data4 from 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `data` where Label = 'CO hr' group by date(timestamp) order by date(timestamp) asc)a 
#left join 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `data` where Label = 'O3 hr' group by date(timestamp) order by date(timestamp) asc) b 
#on a.date = b.date
#left join 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `data` where Label = 'PM2,5 - BAM hr' group by date(timestamp) order by date(timestamp) asc) c 
#on a.date = c.date
#left join 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `data` where Label = 'NOx hr' group by date(timestamp) order by date(timestamp) asc) d
#on a.date = d.date
#order by a.date asc"""

sql = """SELECT date(timestamp) as date, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as data1 FROM `qc_saint_garnier` 
where Label = 'PM2,5 - BAM hr' group by date(timestamp) order by date(timestamp) asc"""

rows = fetchArrayFromSql(sql)
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
#df.rename(columns={0: 'Date', 1: 'data1', 2: 'data2', 3: 'data3', 4:'data4'}, inplace=True);
df.rename(columns={0: 'Date', 1: 'data1'}, inplace=True);

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df['Date'],
                y=df['data1'],
                name="CO hr ppm",
                line_color='deepskyblue',
                opacity=0.8))

"""
fig.add_trace(go.Scatter(
               	x=df['Date'],
                y=df['data2'],
                name="O3 hr",
                line_color='dimgray',
                opacity=0.8))
fig.add_trace(go.Scatter(
               	x=df['Date'],
                y=df['data3'],
                name="PM2,5 - BAM hr",
                line_color='red',
                opacity=0.8))

fig.add_trace(go.Scatter(
               	x=df['Date'],
                y=df['data4'],
                name="SO2 hr",
                line_color='yellow',
                opacity=0.8))
fig.update_layout(title_text="Quebec Parc George")
"""

fig.update_layout(
    title=go.layout.Title(
        text="Quebec Saint Garnier",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Date",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="PM2,5 - BAM hr μg/m3",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )
    )
)

fig.show()