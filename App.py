import pandas as pd # read csv, df manipulation
import plotly.express as px # interactive charts
import streamlit as st # data web application development
 

# streamlit hello in your terminal (Streamlit website)
df=pd.read_csv(r'Results.csv',sep=',',  header=0, names=None, index_col=None, usecols=None, skiprows=None, nrows=None)
df.columns=['date','Test','Regression','Ridge','Polynomial'] # For manipulating data and not for the app purpose

#df['avg']=df['Ridge'].mean()
#df['max_Reg']=df['Regression'].max()
#df['asis']=df['Regression'].iloc[-1]



st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="Active",
    layout="wide",
)

st.title('Macroeconomic Analysis')
st.markdown('This dashboard will help you get more information about the GDP and Reserves and plots the results')

# Create the Filter first:

# top-level filters
job_filter = st.selectbox("Select the Job", pd.unique(df['Test']))
# dataframe filter
df = df[df['Test'] == job_filter]

period=df['date'].iloc[-1]
# KPI
col1, col2, col3=st.columns(3)

with col1:
    st.metric(
        label = 'GDP',
        value = round (df['Ridge'].mean())     # Rounding here eliminates decimals.
)

with col2:
    st.metric(
        label = 'Reserves',
        value = int(df['Regression'].mean())
)

with col3:
    st.metric(
        label = 'FDI',
        value = f'$ {period}'
)

#job_filter = st.selectbox ('Select the status', pd.unique (df['Polynomial']))
#d= df [df ['Polynomial'] == status_filter]

# Creating two Columns (Spaces)
# print(df.dtypes)
# df['date'] = pd.to_numeric(df['date'])
df = df.astype({'date':'int'})


fig_col1, fig_col2,fig_col3= st.columns([0.45,0.45,0.1])
# width and length 400 default.

with fig_col1:
    st.markdown("First Chart")
    fig1 = px.histogram(data_frame=df, x="Ridge")
    st.write(fig1)

with fig_col2:
    st.markdown("##### Second Chart")
    fig2 = px.histogram(data_frame=df, x="Regression")
    st.write(fig2)

with fig_col1:
    st.markdown("Graph")
    fig3 = px.line(df, x='date', y=df.columns[2:], width=1200)
    st.write(fig3)


# Show a Table
#st.markdown('### Detailed View')
#st.dataframe(df)


# streamlit run app.py           - in Terminal
