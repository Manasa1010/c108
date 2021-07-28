import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
print(df)

h=df["Height(Inches)"].tolist()
print(h)


fig=ff.create_distplot([h],["index"],show_hist=False)
fig.show()

