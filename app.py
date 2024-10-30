import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Altair as alt
#st.title('Streamlit First Activity!')
#st.write('submited by:Anahid')
penguins = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/main/data/penguins.csv')
#st.scatter_chart(data=penguins,x='flipper_length_mm',y='body_mass_g',x_label='Flipper Length' ,y_label='Body Mass(g)',color='species')

#st.bar_chart(data=penguins, x='species', y='culmen_depth_mm', x_label='Culmen Depth(mm)', y_label='Species', color='sex',horizontal=True)

#stock = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/stocks.csv')
#st.line_chart(stock, x="date", y="price", color="symbol",x_label='Date', y_label='Price')
data =penguins
st.sidebar.header("select options")
selected_category = st.sidebar.selectbox("select series:",options=['All','Adelie','Gentoo'])

if selected_category != 'All':
    filtered_data=data[data['species']== selected_category]
else:
    filtered_data = data

st.write("### Matpilot Histogram")
fig, ax= plt.subplots()
ax.hist(filtered_data['culmen_length_mm'],bins=30,color="skyblue",edgecolor="black")
ax.set_title("Matpilot His for Culmen Length")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

st.pyplot(fig)

st.write("##Seaborn Density Plot")
fig,ax = plt.subplots()
fig = sns.displot(filtered_data['culmen_length_mm'],color="skyblue",kind='kde',ax=ax,fill=True)
ax.set_xlabel("Value")
ax.set_ylabel("Density")
st.pyplot(fig)

#install Atair
st.write("Altaire")
scatter_plot = alt.Chart(filtered_data).mark_circle().encode(
    x= alt.X('flipper_length_mm',title='Flipper Length'),
    y=alt.Y('body_mass_g',title='Body Mass'),
    color=alt.Color('island',scale=alt.Scale(scheme='tableau10')),
    tooltip=['island','flipper_length_mm','ody_mass_g']

).properties(
    width=600,
    height=400,
    title="Scatter Plot"
).interactive()
st.altair_chart(scatter_plot,use_container_width=True)

#pip install pipreqs give your requirments
#requirments.txt