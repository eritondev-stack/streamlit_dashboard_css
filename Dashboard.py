import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_extras.grid import grid
import altair as alt
import numpy as np
from extras import ancora, loadCss, padding
from progress_circular_bar import circular_progress_bar
from render_html import render_html
from custom_table import custom_table
import plotly.graph_objects as go
import streamlit.components.v1 as components
import matplotlib.pyplot as plt


st.set_page_config(page_title="Dashboard Civeis",
page_icon="🧊",
layout="wide",
initial_sidebar_state="auto")

loadCss()

st.header("Dashboard Tivio")

@st.cache_data(show_spinner="Carregando os dados...")
def getDatabase():
    df = pd.read_csv('./dataset/Billionaires Statistics Dataset.csv')
    return df

df = getDatabase()

st.session_state.df_civeis = df


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

number = 90
with st.sidebar:
    number = st.number_input('Insert a number', step=1, value=number)
    
grid1 = grid([1,1,1,1],[1,1], vertical_align="center")

with grid1.container():
    ancora("ancora")
    st.markdown("<div class='conciliado'>Conciliado - Conta 8 </div>", unsafe_allow_html=True)
    padding(1)
    circular_progress_bar(value=number, width=130, pathColor='#14b8a6', key="c-1")
    render_html("""
        <div class='w-full flex flex-row justify-center items-center gap-4'>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Linhas</span>
                <span>120</span>
            </div>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Diferença</span>
                <span>R$: 1.400.500,75</span>
            </div>
        </div>
""", "r-1")
    
with grid1.container():
    ancora("ancora")
    st.markdown("<div class='conciliado'>Conciliado - Conta 8</div>", unsafe_allow_html=True)
    padding(1)
    circular_progress_bar(value=number, width=130, pathColor='#14b8a6', key="c-2")
    render_html("""
        <div class='w-full flex flex-row justify-center items-center gap-4'>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Linhas</span>
                <span>120</span>
            </div>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Diferença</span>
                <span>R$: 1.400.500,75</span>
            </div>
        </div>
""", "r-2")
    
with grid1.container():
    ancora("ancora")
    st.markdown("<div class='conciliado'>Conciliado - Conta 8</div>", unsafe_allow_html=True)
    padding(1)
    circular_progress_bar(value=number, width=130, pathColor='#14b8a6', key="c-3")
    render_html("""
        <div class='w-full flex flex-row justify-center items-center gap-4'>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Linhas</span>
                <span>120</span>
            </div>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Diferença</span>
                <span>R$: 1.400.500,75</span>
            </div>
        </div>
""", "r-3")
    
    
with grid1.container():
    ancora("ancora")
    st.markdown("<div class='conciliado'>Total Conciliado</div>", unsafe_allow_html=True)
    padding(1)
    circular_progress_bar(value=number, width=130, pathColor='#a855f7', key="c-4")
    render_html("""
        <div class='w-full flex flex-row justify-center items-center gap-4'>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Linhas</span>
                <span>120</span>
            </div>
            <div class="flex flex-col justify-center items-center">
                <span class="text-gray-500 text-sm">Diferença</span>
                <span>R$: 1.400.500,75</span>
            </div>
        </div>
""", "r-4")



 
source = pd.DataFrame({
    'Meses': ['01-Jan', '02-Fev', '03-Mar', '04-Abr', '05-Mai', '06-Jun', '07-Jul'],
    'DJUR': [25, 57, 23, 19, 8, 47, 8],
    'Contabil': [25, 57, 23, 23, 8, 55, 12],
})
colors = ['#a855f7'] * 7
colors[6] = "#2563eb"
config = {'displayModeBar': False}


             
# update_layout(
#                           plot_bgcolor='white',
#                           paper_bgcolor='white',
# )  

        
fig3 = go.Figure()
fig3.update_layout(yaxis_range=[0,2.4])
x_data = [0, 1, 2, 3, 4, 5, 6, 7]
y_data = [1.5, 1, 1.3, 0.7, 0.8, 0.9, 1, 1]


colors1 = ['#a855f7'] * 8
colors1[7] = "#2563eb"
fig3.add_trace(
    go.Bar(
        x=x_data,
        y=y_data,
        name="DJUR",
        showlegend=False,
    )).update_traces(marker_color=colors1, showlegend=False)


# Target
x0_inicial = -0.4
x1_inicial =  0.4

for index, item in enumerate(y_data):
    fig3.add_shape(type="line",
    x0=x0_inicial, y0=item + 0.5, x1=x1_inicial, y1=item + 0.5,
    name="Contabil",
    showlegend= False if index == 0 else False,
    line=dict(color="red",width=3),
    label=dict(
        text=f"{str(item)}M", font=dict(size=15)
    ))
    x0_inicial = x0_inicial + 1
    x1_inicial = x1_inicial + 1


# Label
x0_inicial = -0.4
x1_inicial =  0.4

for index, item in enumerate(y_data):
    fig3.add_shape(type="line",
    x0=x0_inicial, y0=(item/2) - 0.10, x1=x1_inicial, y1=(item/2) - 0.10,
    name="Contabil",
    showlegend= False if index == 0 else False,
    line=dict(color="red",width=0),
    label=dict(
        text=f"{str(item)}M", font=dict(size=15, color="white")
    ))
    x0_inicial = x0_inicial + 1
    x1_inicial = x1_inicial + 1

    

with grid1.container():
    ancora("ancora")
    #padding(80)
    st.plotly_chart(fig3, use_container_width=True, config=config)

df_pagm = pd.DataFrame({
    'x': [10, 9, 8,7,6, 5],
    'y': ['Acordo', 'Acordo pós...', 'Honorarios', 'Condenação', 'Condenação pós...', 'Garantia']
})
   
fig7 = go.Figure(go.Bar(
            x=df_pagm['x'],
            y=df_pagm['y'],
            orientation='h',
            )).update_layout(xaxis_range=[0,12], yaxis = dict( tickfont = dict(size=15)))
# Label
y_inicial = -0.3

for index, item in enumerate(df_pagm['x']):
    print(item)
    fig7.add_shape(type="line",
    x0=item/2, y0=y_inicial, x1=item/2, y1=y_inicial,
    name="Contabil",
    showlegend= False,
    line=dict(color="red",width=0),
    label=dict(
        text=f"{str(item)}M", font=dict(size=15, color="white")
    ))
    y_inicial = y_inicial + 1


with grid1.container():
    ancora("ancora")
    #padding(80)
    st.plotly_chart(fig7, use_container_width=True, config=config)


# fig6 = px.pie(source, values='DJUR', names="Meses", hole=.0)

    
# with grid1.container():
#     ancora("ancora")
#     #padding(80)
#     st.plotly_chart(fig6, use_container_width=True, config=config)
    
    
# list_dict = []
# for index, row in list(source.iterrows()):
#     list_dict.append(dict(row))
# st.json(list_dict)

out = df.head(200).to_json(orient='records')
custom_table(out, "C-23")






        
        


   

