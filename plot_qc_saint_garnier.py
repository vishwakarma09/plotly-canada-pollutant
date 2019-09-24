import plotly.graph_objects as go
from plotly.subplots import make_subplots
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


#sql = """select a.date, ifnull(a.average,0) as data1, ifnull(b.average,0) as data2, ifnull(c.average,0) as data3, ifnull(d.average,0) as data4 from 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_levis_chamy` where Label = 'CO hr' group by date(timestamp) order by date(timestamp) asc)a 
#left join 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_levis_chamy` where Label = 'O3 hr' group by date(timestamp) order by date(timestamp) asc) b 
#on a.date = b.date
#left join 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_levis_chamy` where Label = 'PM2,5 - BAM hr' group by date(timestamp) order by date(timestamp) asc) c 
#on a.date = c.date
#left join 
#(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_levis_chamy` where Label = 'NOx hr' group by date(timestamp) order by date(timestamp) asc) d
#on a.date = d.date
#order by a.date asc"""

sql = """select a.date, ifnull(a.average,0) as data1, ifnull(b.average,0) as data2, ifnull(c.average,0) as data3, ifnull(d.average,0) as data4 from 
(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_saint_garnier` where Label = 'O3 hr' group by date(timestamp) order by date(timestamp) asc)a 
left join 
(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_saint_garnier` where Label = 'O3 hr' group by date(timestamp) order by date(timestamp) asc) b 
on a.date = b.date
left join 
(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_saint_garnier` where Label = 'NOx hr' group by date(timestamp) order by date(timestamp) asc) c 
on a.date = c.date
left join 
(SELECT date(timestamp) as date, Label, EXP( SUM( LOG( value ) ) / COUNT( * ) ) as average FROM `qc_saint_garnier` where Label = 'NOx hr' group by date(timestamp) order by date(timestamp) asc) d
on a.date = d.date
order by a.date asc"""
rows = fetchArrayFromSql(sql)
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Date', 1: 'data1', 2: 'data2', 3: 'data3', 4:'data4'}, inplace=True);

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=df['Date'], y=df['data1'], name="O3 hr"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['Date'], y=df['data3'], name="NOx hr"),
    secondary_y=True,
)

"""
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['data2'], name="O3 hr"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['Date'], y=df['data4'], name="NOx hr"),
    secondary_y=True,
)
"""

# Add figure title
fig.update_layout(
    title_text="Quebec Saint Garnier"
)

# Set x-axis title
fig.update_xaxes(title_text="date")

# Set y-axes titles

"""
fig.update_yaxes(title_text="CO hr ppm", secondary_y=False)
fig.update_yaxes(title_text="PM2,5 - BAM hr μg/m3", secondary_y=True)

"""
fig.update_yaxes(title_text="O3 hr ppb", secondary_y=False)
fig.update_yaxes(title_text="NOx hr ppb", secondary_y=True)

fig.show()