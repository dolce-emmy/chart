import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Technology': ['HTML', 'CSS', 'JavaScript', 'React.js', 'MongoDB'],
    'Usage': [30, 20, 25, 15, 10]
}

df = pd.DataFrame(data)

# Create a pie chart with invisible values
fig = px.pie(df, names='Technology', values='Usage', title='Technology Usage Distribution')

# Hide values by setting text attribute to an empty list
fig.update_traces(textinfo='none', textposition='inside')

# Save the chart as an HTML file
fig.write_html("technology_pie_chart.html")
