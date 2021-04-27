import streamlit as st
# import pandas as pd
# import numpy as np
import streamlit.components.v1 as components

# x= st.slider('x', max_value=1000)
# st.write(x, 'squared is', x*x)
# df = pd.read_excel('Biker_Utilization_Mar2021_new.xlsx')
# st.header('Welcome Home')
# st.write(df)
# cols = df.columns
# st.write(cols)
# st.write(df.astype(object))
#uniq = df['biker_name'].drop_duplicates()
# st.write(np.count_nonzero(uniq))
# st.write(np.count_nonzero(df['biker_name'].drop_duplicates()))
st.sidebar.title('Analytics Dashboard')
st.sidebar.markdown('Multiple reports for each department will be displayed here')
box = st.sidebar.selectbox('', ('Home', 'HR', 'DevOps', 'CRM', 'Delivery'))


def main():
    html_temp = """<script type='text/javascript' src='https://prod-apnortheast-a.online.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 1550px; height: 3027px;'><object class='tableauViz' width='1550' height='3027' style='display:none;'><param name='host_url' value='https%3A%2F%2Fprod-apnortheast-a.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;dataviewingtester0890' /><param name='name' value='BikerPatternDashboard-rev&#47;BikerWorkPattern' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>"""
    components.html(html_temp, width=3000, height=2500, scrolling=False)

if box == 'Delivery':
    st.header('Welcome to Delivery Section')
    main()

elif box == 'HR':
    st.header('Welcome HR')
    st.markdown('hi')

elif box == 'Home':
    st.header('Welcome Home')

elif box == 'CRM':
    st.header('Welcome CRM')

elif box == 'DevOps':
    st.header('Welcome DevOps')
