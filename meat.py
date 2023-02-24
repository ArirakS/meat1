import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib
st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz1X8Uw4W5iD1MmsyRVgKdalmtd8uMDas3mw&usqp=CAU");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 0.3; */
       }}
       </style>
       """,

    unsafe_allow_html=True
)


st.title(':red[Meet Meat]')

st.markdown('เว็บไซต์ที่บอกข้อมูลราคาเนื้อไก่และเนื้อหมู')
st.markdown('เราได้รวบรวมราคาเนื้อไก่และหมูมาให้คุณดูประกอบการตัดสินใจก่อนที่จะไปตลาด')

def load_meat_data():
    return pd.read_csv('meat.csv')

def save_model(model):
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')
def scatter_data():
  #  Adp = pd.read_csv('data.csv')

# สร้างกราฟด้วย Matplotlib
    fig, ax = plt.subplots()
    for category, group in Adp.groupby('type of meat'):
       ax.scatter(group['weight'], group['price'])
    ax.legend()
    ax.set_xlabel('weight', fontsize=13)
    ax.set_ylabel('price', fontsize=13)
    st.pyplot(fig)


col1, col2 = st.columns((1.5,2))

st.markdown(
    """
    <style>
    div.stButton > button:first-child{
        background-color:#99FFCC;
        width: 150px;
        height: 30px;
        }
        <style>
        """,
    unsafe_allow_html=True
)


Adp = load_meat_data()
generate = st.button('generate meat.csv')
if generate:
    col1.write('generating "meat.meat" ...')
    col1.write(' ... done')

load = col1.button('load meat.csv')
matplotlib.rc('font', family='TH Sarabun New')
st.dataframe(Adp)
scatter_data()

with st.container():
    image_col, button_col = st.columns((1,3))
    col2.image('https://www.matichon.co.th/wp-content/uploads/2021/08/01-99.jpg', width=300)
    col2.markdown('[ที่มา](https://www.matichon.co.th/publicize/news_2888144)')

col2.write('ราคาเนื้อ')

if load:
    col1.write('loading "meat.csv ..."')
    col1.write('... done')
    col1.dataframe(Adp)
   # fig, ax = plt.subplots()
   # Adp.plot.scatter(x='x', y='y', ax=ax)
   # st.pyplot(fig)

meat_fucntion = col1.selectbox("เลือกประเภทเนื้อ", ('หมูสามชั้น', 'หมูเนื้อแดง', 'หมูสันนอก', 'หมูสันใน', 'หมูบด', 'อกไก่', 'ปีกเต็มไก่', 'น่องไก่','ขาไก่' ))
train = col1.button('train')
if train:
    col1.write('training model ...')
    Adp = Adp.loc[Adp['type of meat'] == meat_fucntion]
    X = Adp['weight'].values.reshape(-1, 1)
    y = Adp['price'].values
    model = LinearRegression()
    model.fit(X, y)
    save_model(model)

#button = st.button('เสร็จสิ้น')

kilogram = col1.number_input('กรุณาใส่น้ำหนักที่ต้องการ')
model = load_model()
predict = model.predict([[kilogram]])
button = col1.button('เสร็จสิ้น')
if meat_fucntion == 'หมูสามชั้น':
     st.markdown(f"""
     น้ำหนัก{kilogram} และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'หมูเนื้อแดง':
     st.markdown(f"""
     น้ำหนัก{kilogram}และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'หมูสันนอก':
     st.markdown(f"""
     น้ำหนัก{kilogram} และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'หมูสันใน':
     st.markdown(f"""
     น้ำหนัก{kilogram} และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'หมูบด':
     st.markdown(f"""
     น้ำหนัก{kilogram}และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'อกไก่':
     st.markdown(f"""
     น้ำหนัก{kilogram}และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'ปีกเต็มไก่':
     st.markdown(f"""
     น้ำหนัก{kilogram}และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'น่องไก่':
     st.markdown(f"""
     น้ำหนัก{kilogram}และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
     โดยมีราคาเท่ากับ {predict[0]} """)
elif meat_fucntion == 'ขาไก่':
     st.markdown(f"""
          น้ำหนัก{kilogram}และประเภทเนื้อที่คุณเลือกคือ{meat_fucntion}
          โดยมีราคาเท่ากับ {predict[0]} """)