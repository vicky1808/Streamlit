import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
a = []
m = []
n = []
mother = []
contact = []
std = []
date1 = []

data = pd.DataFrame({"Name":[a],"Last Name":[n],"Fathers Name":[m],"Mothers Name":[mother],"Contact no":[contact],"Admission Class":[std],"Date of Admission":[date1]})
def action1(b):
    a.append(b)
def action2(c):
    m.append(c)
def action3(d):
    n.append(d)
def action4(mother1):
    mother.append(mother1)
def action5(phone):
    contact.append(phone)
def action6(admission):
    std.append(admission)
def action7(date2):
    date1.append(date2)

st.set_page_config(page_title="NS coaching",page_icon="nslogo.jpg")
with st.sidebar:
    selected = option_menu(menu_title="Main Menu",options=["About us", "Admission Form", "Fees","Contact"],icons=["house", "book","currency-rupee","envelope"],
                       menu_icon="cast",default_index=0)

if selected == "About us":
    col5,col6,col7,col8,col9=st.columns(5)
    with col7:
        st.image("nslogo.jpg")
    st.title(":blue[Welcome To NS Coaching]")
    ab,bc=st.columns(2)
    with bc:
        st.subheader(":green[---Bridge for Success]")
    st.title("NS Empowering Students Since 2008")

    st.markdown(":red[**ABOUT US**] - Established in 2008, NS has been a pioneer in nurturing students' holistic development. With a steadfast commitment to excellence, we have become a trusted partner in shaping the future of countless individuals. Our three pillars of focus – Knowledge, Health, and Behavior – form the foundation upon which we build success stories.")
    st.markdown(":orange[**OUR APPROACH**] - At NS, we believe in going beyond conventional education. We strive to cultivate a balanced blend of knowledge, mental well-being, and exemplary conduct in our students. Through our comprehensive programs, we aim to equip them with the skills and resilience needed to thrive in todays competitive world.")
    st.markdown(":violet[**OUR MISSION**] - Our mission is simple yet profound: to provide quality education, instill moral values, and promote mental wellness among our students. We are dedicated to nurturing not just academic achievers but also compassionate and well-rounded individuals who contribute positively to society.")

if selected == "Admission Form":
    vv,ww,xx,yy,zz=st.columns(5)
    with xx:
        st.image("nslogo.jpg")
    st.title(":blue[Welcome To NS Coaching]")
    pq,qr=st.columns(2)
    with qr:
        st.subheader(':green[---Bridge for Success]')
    st.write("---")
    st.subheader(":red[PERSONAL INFORMATION]")
    col1,col2=st.columns(2)
    with col1:
        z = st.text_input('First Name :')
        q = st.text_input('Fathers Name :')
    with col2:
        r = st.text_input('Last Name :')
        mom_name=st.text_input('Mothers Name :')
    st.text_area('Address')
    mobile = st.text_input('Contact No')
    date = st.date_input("Date of Admission : ",value=None)
    st.radio('Gender',['Male','Female','Transgender'])
    standard = st.selectbox('Admission for Std',['7th','8th','9th','10th','11th sci','11th Com','12th Sci','12th Com'])
    if st.button('Submit'):
        action1(z)
        action2(q)
        action3(r)
        action4(mom_name)
        action5(mobile)
        action6(standard)
        action7(date)

    st.write(data)


if selected == "Fees":
    pp,qq,rr,ss,tt=st.columns(5)
    with rr:
        st.image("nslogo.jpg")
    st.title(":blue[Welcome To NS Coaching]")
    xy,yz=st.columns(2)
    with yz:
        st.subheader(':green[---Bridge for Success]')
    st.write("---")
    st.subheader(":red[FEES STRUCTURE FOR EACH SECTION]")
    df=pd.read_csv("Fees.csv")
    st.dataframe(df,width=700)

if selected == "Contact":
    aa,bb,cc,dd,ee=st.columns(5)
    with cc:
        st.image("nslogo.jpg")
    st.title(":blue[Welcome To NS Coaching]")
    gh,hi=st.columns(2)
    with hi:
        st.subheader(':green[---Bridge for Success]')
    st.divider()
    st.subheader(":violet[Have any Questions ? We would like to hear from you]")
    col3,col4=st.columns(2)
    with col3:
        st.subheader(":red[Location]")
        st.write("Want to visit our institute for more queries")
        st.link_button(" Press Location","https://www.google.com/maps/search/numstats+coaching+location/@19.0395412,72.8574956,16z?entry=ttu")
    with col4:
        st.subheader(":orange[Help & Support]")
        st.write("Our support team is available.Contact us by below number and email-id")
        st.write("Contact no : 63603XXXXX")
        st.write("Email-id : nsclasses@gmail.com")
    st.subheader(":violet[For demo lecture videos go through by clicking the below button]")
    st.link_button("Demo Sessions","https://www.youtube.com/@numstatscoaching5237")