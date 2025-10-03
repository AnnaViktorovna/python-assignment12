import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))


df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)

fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title='Strength vs. Frequency by Wind Direction')

fig.update_layout(
    xaxis_title='Wind Strength',
    yaxis_title='Frequency',
)


fig.write_html('wind.html', auto_open=True)

print("Plot saved as wind.html")