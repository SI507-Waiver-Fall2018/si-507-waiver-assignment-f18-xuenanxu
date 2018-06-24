# Name: Xuenan Xu
# uniqname: xuenanxu
# UMID: 35069066

# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.offline as offline
import plotly.graph_objs as go
import csv

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

#online way
# sign in plotly
py.sign_in('xuenanxu', 'DXR4YMyXnq4HjKssVzCT')

word = []
freq = []

with open("noun_data.csv", "r", encoding='utf8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        word.append(row["Noun"])
        freq.append(int(row["Number"]))

data = [go.Bar(
            x = word,
            y = freq)]

layout = go.Layout(title = "Five Most Frequent Nouns")

#image file in png with be downloaded to the root folder
fig = go.Figure(data = data, layout = layout)
py.image.save_as(fig, filename = "part4_viz_image.png")