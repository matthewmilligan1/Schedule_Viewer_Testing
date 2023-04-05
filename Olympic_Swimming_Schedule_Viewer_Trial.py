#Imports

import os
import streamlit as st
import pandas as pd
import plotly as px
import pyautogui

password = "Olympic2024!"

validation = pd.read_excel('Validation.xlsx')

Swimmer_List = validation['Swimmer'].unique()

Coach_List = validation['Coach'].unique()


Event_List = ['50 BCK (M)', 
              '50 BCK (F)',
              '50 BRS (M)',
              '50 BRS (F)',
              '50 FLY (M)',
              '50 FLY (F)',
              '50 FS (M)',
              '50 FS (F)',
              '100 BCK (M)',
              '100 BCK (F)',
              '100 BRS (M)',
              '100 BRS (F)',
              '100 FLY (M)',
              '100 FLY (F)',
              '100 FS (M)',
              '100 FS (F)',
              '200 BCK (M)',
              '200 BCK (F)',
              '200 BRS (M)',
              '200 BRS (F)',
              '200 FLY (M)',
              '200 FLY (F)',
              '200 FS (M)',
              '200 FS (F)',
              '400 FS (M)',
              '400 FS (F)',
              '800 FS (M)',
              '800 FS (F)',
              '1500 FS (M)',
              '1500 FS (F)',
              '200 IM (M)',
              '200 IM (F)',
              '400 IM (M)',
              '400 IM (F)',
              '4x100 FS (M)',
              '4x100 FS (F)',
              '4x100 FS (MX)',
              '4x100 MED (M)',
              '4x100 MED (F)',
              '4x100 MED (MX)',
              '4x200 FS (M)',
              '4x200 FS (F)']



#Setting config

st.set_page_config(layout='wide', initial_sidebar_state='expanded')



#Side bar

st.sidebar.header('Control Panel')
st.sidebar.markdown("""---""")
st.sidebar.subheader('Login Section')

Password_Provided = st.sidebar.text_input("Input Password & click access button to open viewer", type='password')
Login_Button = st.sidebar.button("Access App")
if Password_Provided == password:
    st.sidebar.write('Current Status: Access Granted')
else:
    st.sidebar.write('Current Status: Access Denied')
st.sidebar.markdown("""---""")

st.sidebar.subheader('Viewing Section')
Viewer_Method = st.sidebar.radio('Select view method:', options=['Swimmer View', 'Coach View', 'Hypothetical View'])

if Viewer_Method == 'Swimmer View':
    Swimmer_Select = st.sidebar.selectbox('Select a Swimmer to see specific event entries:', Swimmer_List)
elif Viewer_Method == 'Coach View':
    Coach_Select = st.sidebar.selectbox('Select a Coach to see specific event entries:', Coach_List)
elif Viewer_Method == 'Hypothetical View':
    Swimmer_Select = st.sidebar.selectbox('Select a Swimmer to see specific event entries:', Swimmer_List)
    Event_Select = st.sidebar.multiselect('Select event(s) to create specific hypothetical schedule:', Event_List)
st.sidebar.markdown("""---""")

st.sidebar.subheader('Export Information')
if st.sidebar.button('Export or print page as pdf'):
    pyautogui.hotkey('ctrl', 'p')






def Access_Denied():
    
    #Setting containers

    main_overview = st.container()

    with main_overview:
        st.image('https://www.britishswimming.org/media/images/BritishSwimming-OneTeam-Colour.original.png')
        st.title("World Championships Schedule Viewer")
        st.subheader("App access not currently granted.....Please enter password in sidebar to proceeed to App")





def Swimmer_View():

    #Dataset manipulation

    swimmer_dataset = pd.read_excel('RAW Timetable.xlsx')

    Swimmer_List = validation['Swimmer'].unique()

    if Swimmer_Select == "No Selection":
        swimmer_dataset['Swimmer'] = "No Selection"
    elif Swimmer_Select != "No Selection":
        swimmer_dataset = pd.merge(swimmer_dataset, validation, on='Event', how='left')
        swimmer_dataset = swimmer_dataset.drop(['id', 'Coach', 'Athlete Pic URL', 'Coach Pic URL'], axis=1)


    swimmer_dataset = swimmer_dataset.drop(['Event Letter', 'Unique ID', 'Venue', 'Date', 'Session Country Start', 'Session Country Finish', 'Gender', 'Stage'], axis=1)

    swimmer_dataset['Event Start'] = swimmer_dataset['Event Start'].apply(str).str[0:5]
    swimmer_dataset = swimmer_dataset.rename({'Full List Final': 'Event:', 'Event Start': 'Time:'}, axis=1)

    Swimmer_Select_Pic = (validation.loc[(validation['Swimmer'] == Swimmer_Select)]['Athlete Pic URL'].unique())[0]

    swimmer_dataset_filter = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Swimmer'] == Swimmer_Select)])

    session_1 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 1) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    styler = session_1[['Event:', 'Time:']].style.hide_index()

    session_2 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 2) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_3 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 3) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_4 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 4) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_5 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 5) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_6 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 6) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_7 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 7) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_8 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 8) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_9 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 9) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_10 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 10) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_11 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 11) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_12 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 12) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_13 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 13) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])
    session_14 = pd.DataFrame(swimmer_dataset.loc[(swimmer_dataset['Session ID'] == 14) & (swimmer_dataset['Swimmer'] == Swimmer_Select)])

    swimmers_swims_entered = swimmer_dataset_filter.count()[0]
    swimmers_events_entered = swimmer_dataset_filter['Event'].nunique()
    swimmers_metres_covered = swimmer_dataset_filter['Distance'].sum()

    if  Swimmer_Select != "No Selection":
        if session_2.count()[0] > 1:
            session_2_final_event = (float(session_2['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_2['Time:'].iloc[-1].split(':', 1)[1]))
            session_2_first_event = (float(session_2['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_2['Time:'].iloc[0].split(':', 1)[1]))
            session_2_gap = f'{int((session_2_final_event - session_2_first_event))} mins'
            session_2_gap_label = 'Session 2 Race Gap:'
        else:
            session_2_gap = ""
            session_2_gap_label = ''
    else:
        session_2_gap = ""
        session_2_gap_label = ''

    if  Swimmer_Select != "No Selection":
        if session_4.count()[0] > 1:
            session_4_final_event = (float(session_4['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_4['Time:'].iloc[-1].split(':', 1)[1]))
            session_4_first_event = (float(session_4['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_4['Time:'].iloc[0].split(':', 1)[1]))
            session_4_gap = f'{int((session_4_final_event - session_4_first_event))} mins'
            session_4_gap_label = 'Session 4 Race Gap:'
        else:
            session_4_gap = ""
            session_4_gap_label = ''
    else:
        session_4_gap = ""
        session_4_gap_label = ''

    if  Swimmer_Select != "No Selection":
        if session_6.count()[0] > 1:
            session_6_final_event = (float(session_6['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_6['Time:'].iloc[-1].split(':', 1)[1]))
            session_6_first_event = (float(session_6['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_6['Time:'].iloc[0].split(':', 1)[1]))
            session_6_gap = f'{int((session_6_final_event - session_6_first_event))} mins'
            session_6_gap_label = 'Session 6 Race Gap:'
        else:
            session_6_gap = ""
            session_6_gap_label = ''
    else:
        session_6_gap = ""
        session_6_gap_label = ''

    if  Swimmer_Select != "No Selection":
        if session_8.count()[0] > 1:
            session_8_final_event = (float(session_8['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_8['Time:'].iloc[-1].split(':', 1)[1]))
            session_8_first_event = (float(session_8['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_8['Time:'].iloc[0].split(':', 1)[1]))
            session_8_gap = f'{int((session_8_final_event - session_8_first_event))} mins'
            session_8_gap_label = 'Session 8 Race Gap:'
        else:
            session_8_gap = ""
            session_8_gap_label = ''
    else:
        session_8_gap = ""
        session_8_gap_label = ''

    if  Swimmer_Select != "No Selection":
        if session_10.count()[0] > 1:
            session_10_final_event = (float(session_10['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_10['Time:'].iloc[-1].split(':', 1)[1]))
            session_10_first_event = (float(session_10['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_10['Time:'].iloc[0].split(':', 1)[1]))
            session_10_gap = f'{int((session_10_final_event - session_10_first_event))} mins'
            session_10_gap_label = 'Session 10 Race Gap:'
        else:
            session_10_gap = ""
            session_10_gap_label = ''
    else:
        session_10_gap = ""
        session_10_gap_label = ''

    if  Swimmer_Select != "No Selection":
        if session_12.count()[0] > 1:
            session_12_final_event = (float(session_12['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_12['Time:'].iloc[-1].split(':', 1)[1]))
            session_12_first_event = (float(session_12['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_12['Time:'].iloc[0].split(':', 1)[1]))
            session_12_gap = f'{int((session_12_final_event - session_12_first_event))} mins'
            session_12_gap_label = 'Session 12 Race Gap:'
        else:
            session_12_gap = ""
            session_12_gap_label = ''
    else:
        session_12_gap = ""
        session_12_gap_label = ''

    if  Swimmer_Select != "No Selection":
        if session_14.count()[0] > 1:
            session_14_final_event = (float(session_14['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_14['Time:'].iloc[-1].split(':', 1)[1]))
            session_14_first_event = (float(session_14['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_14['Time:'].iloc[0].split(':', 1)[1]))
            session_14_gap = f'{int((session_14_final_event - session_14_first_event))} mins'
            session_14_gap_label = 'Session 14 Race Gap:'
        else:
            session_14_gap = ""
            session_14_gap_label = ''
    else:
        session_14_gap = ""
        session_14_gap_label = ''


    #Setting containers

    main_overview = st.container()

    with main_overview:
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.image('https://www.britishswimming.org/media/images/BritishSwimming-OneTeam-Colour.original.png')
            st.title("British Swimming World Championships Schedule Viewer")
            st.subheader("Event Timetable by Swimmer:")
    
        with col_2:
            st.image(Swimmer_Select_Pic)

        with col_3:
            st.metric('Events Entered:',str(swimmers_events_entered))
            st.metric('Potential Swims:',str(swimmers_swims_entered))
            st.metric('Potential Metres:',str(swimmers_metres_covered))

    
    st.markdown("""---""")


    body_overview = st.container()

    with body_overview:
        col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric("","23/07", "Session 1")
        session_1_new = session_1[['Event:', 'Time:']]
        session_1_new = session_1_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_1_new.set_index(session_1_new.columns[0]))
                                 
    with col_2:
        st.metric("", "24/07", "Session 3")
        session_3_new = session_3[['Event:', 'Time:']]
        session_3_new = session_3_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_3_new.set_index(session_3_new.columns[0]))
     
    with col_3:
        st.metric("", "25/07", "Session 5")
        session_5_new = session_5[['Event:', 'Time:']]
        session_5_new = session_5_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_5_new.set_index(session_5_new.columns[0]))

    with col_4:
        st.metric("", "26/07", "Session 7")
        session_7_new = session_7[['Event:', 'Time:']]
        session_7_new = session_7_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_7_new.set_index(session_7_new.columns[0]))

    with col_5:
        st.metric("", "27/07", "Session 9")
        session_9_new = session_9[['Event:', 'Time:']]
        session_9_new = session_9_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_9_new.set_index(session_9_new.columns[0]))
    
    with col_6:
        st.metric("", "28/07", "Session 11")
        session_11_new = session_11[['Event:', 'Time:']]
        session_11_new = session_11_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_11_new.set_index(session_11_new.columns[0]))

    with col_7:
        st.metric("", "29/07", "Session 13")
        session_13_new = session_13[['Event:', 'Time:']]
        session_13_new = session_13_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_13_new.set_index(session_13_new.columns[0]))


    col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric("", "", "Session 2")
        session_2_new = session_2[['Event:', 'Time:']]
        session_2_new = session_2_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_2_new.set_index(session_2_new.columns[0]))
        
    with col_2:
        st.metric("", "", "Session 4")
        session_4_new = session_4[['Event:', 'Time:']]
        session_4_new = session_4_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_4_new.set_index(session_4_new.columns[0]))
        
    with col_3:
        st.metric("", "", "Session 6")
        session_6_new = session_6[['Event:', 'Time:']]
        session_6_new = session_6_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_6_new.set_index(session_6_new.columns[0]))

    with col_4:
        st.metric("", "", "Session 8")
        session_8_new = session_8[['Event:', 'Time:']]
        session_8_new = session_8_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_8_new.set_index(session_8_new.columns[0]))

    with col_5:
        st.metric("", "", "Session 10")
        session_10_new = session_10[['Event:', 'Time:']]
        session_10_new = session_10_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_10_new.set_index(session_10_new.columns[0]))
    
    with col_6:
        st.metric("", "", "Session 12")
        session_12_new = session_12[['Event:', 'Time:']]
        session_12_new = session_12_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_12_new.set_index(session_12_new.columns[0]))

    with col_7:
        st.metric("", "", "Session 14")
        session_14_new = session_14[['Event:', 'Time:']]
        session_14_new = session_14_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_14_new.set_index(session_14_new.columns[0]))
    
    
    col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric(session_2_gap_label, session_2_gap)

    with col_2:
        st.metric(session_4_gap_label, session_4_gap)

    with col_3:
        st.metric(session_6_gap_label, session_6_gap)

    with col_4:
        st.metric(session_8_gap_label, session_8_gap)

    with col_5:
        st.metric(session_10_gap_label, session_10_gap)

    with col_6:
        st.metric(session_12_gap_label, session_12_gap)

    with col_7:
        st.metric(session_14_gap_label, session_14_gap)
        




def Coach_View():

    #Dataset manipulation

    coach_dataset = pd.read_excel('RAW Timetable.xlsx')

    Coach_List = validation['Swimmer'].unique()

    if Coach_Select == "No Selection":
        coach_dataset['Coach'] = "No Selection"
    elif Coach_Select != "No Selection":
        coach_dataset = pd.merge(coach_dataset, validation, on='Event', how='left')
        coach_dataset = coach_dataset.drop(['id', 'Athlete Pic URL', 'Coach Pic URL'], axis=1)


    coach_dataset = coach_dataset.drop(['Event Letter', 'Unique ID', 'Venue', 'Date', 'Session Country Start', 'Session Country Finish', 'Gender', 'Stage'], axis=1)

    coach_dataset['Event Start'] = coach_dataset['Event Start'].apply(str).str[0:5]
    coach_dataset = coach_dataset.rename({'Full List Final': 'Event:', 'Event Start': 'Time:'}, axis=1)

    Coach_Select_Pic = (validation.loc[(validation['Coach'] == Coach_Select)]['Coach Pic URL'].unique())[0]

    coach_dataset_filter = pd.DataFrame(coach_dataset.loc[(coach_dataset['Coach'] == Coach_Select)])

    session_1 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 1) & (coach_dataset['Coach'] == Coach_Select)])
    session_2 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 2) & (coach_dataset['Coach'] == Coach_Select)])
    session_3 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 3) & (coach_dataset['Coach'] == Coach_Select)])
    session_4 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 4) & (coach_dataset['Coach'] == Coach_Select)])
    session_5 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 5) & (coach_dataset['Coach'] == Coach_Select)])
    session_6 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 6) & (coach_dataset['Coach'] == Coach_Select)])
    session_7 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 7) & (coach_dataset['Coach'] == Coach_Select)])
    session_8 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 8) & (coach_dataset['Coach'] == Coach_Select)])
    session_9 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 9) & (coach_dataset['Coach'] == Coach_Select)])
    session_10 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 10) & (coach_dataset['Coach'] == Coach_Select)])
    session_11 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 11) & (coach_dataset['Coach'] == Coach_Select)])
    session_12 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 12) & (coach_dataset['Coach'] == Coach_Select)])
    session_13 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 13) & (coach_dataset['Coach'] == Coach_Select)])
    session_14 = pd.DataFrame(coach_dataset.loc[(coach_dataset['Session ID'] == 14) & (coach_dataset['Coach'] == Coach_Select)])


    coach_swimmers_entered = validation[validation.Coach == Coach_Select]['Swimmer'].nunique()
    coach_swims_entered = coach_dataset_filter.count()[0]
    coach_events_entered = coach_dataset_filter['Event'].nunique()
    coach_metres_covered = coach_dataset_filter['Distance'].sum()


    coach_dataset_2 = pd.read_excel('RAW Timetable.xlsx')
    coach_dataset_2['Event Start'] = coach_dataset_2['Event Start'].apply(str).str[0:5]

    validation_2 = pd.read_excel('Validation.xlsx')

    validation_2 = pd.merge(validation_2, coach_dataset_2, on='Event', how='left')

    Day_1 = pd.DataFrame(validation_2.loc[(validation_2['Session ID'] == 2) & (validation_2['Coach'] == Coach_Select)])
    Day_2 = pd.DataFrame(validation_2.loc[(validation_2['Session ID'] == 4) & (validation_2['Coach'] == Coach_Select)])
    Day_3 = pd.DataFrame(validation_2.loc[(validation_2['Session ID'] == 6) & (validation_2['Coach'] == Coach_Select)])
    Day_4 = pd.DataFrame(validation_2.loc[(validation_2['Session ID'] == 8) & (validation_2['Coach'] == Coach_Select)])
    Day_5 = pd.DataFrame(validation_2.loc[(validation_2['Session ID'] == 10) & (validation_2['Coach'] == Coach_Select)])
    Day_6 = pd.DataFrame(validation_2.loc[(validation_2['Session ID'] == 12) & (validation_2['Coach'] == Coach_Select)])
    Day_7 = pd.DataFrame(validation_2.loc[(validation_2['Session ID'] == 14) & (validation_2['Coach'] == Coach_Select)])


    #Setting containers

    main_overview = st.container()

    with main_overview:
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.image('https://www.britishswimming.org/media/images/BritishSwimming-OneTeam-Colour.original.png')
            st.title("British Swimming World Championships Schedule Viewer")
            st.subheader("Event Timetable by Coach:")
    
        with col_2:
            st.image(Coach_Select_Pic)

        with col_3:
            st.metric('Swimmers Entered:', str(coach_swimmers_entered))
            st.metric('Events Entered:',str(coach_events_entered))
            st.metric('Potential Swims:',str(coach_swims_entered))
            st.metric('Potential Metres:',str(coach_metres_covered))

    
    st.markdown("""---""")


    body_overview = st.container()

    with body_overview:
        col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric("","23/07", "Session 1")
        session_1_new = session_1[['Event:', 'Time:']]
        session_1_new = session_1_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_1_new.set_index(session_1_new.columns[0]))
                                 
    with col_2:
        st.metric("", "24/07", "Session 3")
        session_3_new = session_3[['Event:', 'Time:']]
        session_3_new = session_3_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_3_new.set_index(session_3_new.columns[0]))
     
    with col_3:
        st.metric("", "25/07", "Session 5")
        session_5_new = session_5[['Event:', 'Time:']]
        session_5_new = session_5_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_5_new.set_index(session_5_new.columns[0]))

    with col_4:
        st.metric("", "26/07", "Session 7")
        session_7_new = session_7[['Event:', 'Time:']]
        session_7_new = session_7_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_7_new.set_index(session_7_new.columns[0]))

    with col_5:
        st.metric("", "27/07", "Session 9")
        session_9_new = session_9[['Event:', 'Time:']]
        session_9_new = session_9_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_9_new.set_index(session_9_new.columns[0]))
    
    with col_6:
        st.metric("", "28/07", "Session 11")
        session_11_new = session_11[['Event:', 'Time:']]
        session_11_new = session_11_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_11_new.set_index(session_11_new.columns[0]))

    with col_7:
        st.metric("", "29/07", "Session 13")
        session_13_new = session_13[['Event:', 'Time:']]
        session_13_new = session_13_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_13_new.set_index(session_13_new.columns[0]))


    col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric("", "", "Session 2")
        session_2_new = session_2[['Event:', 'Time:']]
        session_2_new = session_2_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_2_new.set_index(session_2_new.columns[0]))
        
    with col_2:
        st.metric("", "", "Session 4")
        session_4_new = session_4[['Event:', 'Time:']]
        session_4_new = session_4_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_4_new.set_index(session_4_new.columns[0]))
        
    with col_3:
        st.metric("", "", "Session 6")
        session_6_new = session_6[['Event:', 'Time:']]
        session_6_new = session_6_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_6_new.set_index(session_6_new.columns[0]))

    with col_4:
        st.metric("", "", "Session 8")
        session_8_new = session_8[['Event:', 'Time:']]
        session_8_new = session_8_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_8_new.set_index(session_8_new.columns[0]))

    with col_5:
        st.metric("", "", "Session 10")
        session_10_new = session_10[['Event:', 'Time:']]
        session_10_new = session_10_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_10_new.set_index(session_10_new.columns[0]))
    
    with col_6:
        st.metric("", "", "Session 12")
        session_12_new = session_12[['Event:', 'Time:']]
        session_12_new = session_12_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_12_new.set_index(session_12_new.columns[0]))

    with col_7:
        st.metric("", "", "Session 14")
        session_14_new = session_14[['Event:', 'Time:']]
        session_14_new = session_14_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_14_new.set_index(session_14_new.columns[0]))

    
    st.markdown("""---""")


    col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric("", "", "Day 1 Entries:")
        Day_1_new = Day_1[['Swimmer', 'Event']]
        Day_1_new = Day_1_new.rename({'Event': ''}, axis=1)
        st.table(Day_1_new.set_index(Day_1_new.columns[0]))

    with col_2:
        st.metric("", "", "Day 2 Entries:")
        Day_2_new = Day_2[['Swimmer', 'Event']]
        Day_2_new = Day_2_new.rename({'Event': ''}, axis=1)
        st.table(Day_2_new.set_index(Day_2_new.columns[0]))

    with col_3:
        st.metric("", "", "Day 3 Entries:")
        Day_3_new = Day_3[['Swimmer', 'Event']]
        Day_3_new = Day_3_new.rename({'Event': ''}, axis=1)
        st.table(Day_3_new.set_index(Day_3_new.columns[0]))

    with col_4:
        st.metric("", "", "Day 4 Entries:")
        Day_4_new = Day_4[['Swimmer', 'Event']]
        Day_4_new = Day_4_new.rename({'Event': ''}, axis=1)
        st.table(Day_4_new.set_index(Day_4_new.columns[0]))

    with col_5:
        st.metric("", "", "Day 5 Entries:")
        Day_5_new = Day_5[['Swimmer', 'Event']]
        Day_5_new = Day_5_new.rename({'Event': ''}, axis=1)
        st.table(Day_5_new.set_index(Day_5_new.columns[0]))

    with col_6:
        st.metric("", "", "Day 6 Entries:")
        Day_6_new = Day_6[['Swimmer', 'Event']]
        Day_6_new = Day_6_new.rename({'Event': ''}, axis=1)
        st.table(Day_6_new.set_index(Day_6_new.columns[0]))

    with col_7:
        st.metric("", "", "Day 7 Entries:")
        Day_7_new = Day_7[['Swimmer', 'Event']]
        Day_7_new = Day_7_new.rename({'Event': ''}, axis=1)
        st.table(Day_7_new.set_index(Day_7_new.columns[0]))
    




def Hypothetical_View():

    Event_Selection = pd.DataFrame({'Event Select': Event_Select})

    event_dataset = pd.read_excel('RAW Timetable.xlsx')

    event_dataset = pd.merge(event_dataset, Event_Selection, left_on='Event', right_on='Event Select', how='left')

    event_dataset = event_dataset[~event_dataset['Event Select'].isnull()]

    event_dataset['Event Start'] = event_dataset['Event Start'].apply(str).str[0:5]

    event_dataset = event_dataset.rename({'Full List Final': 'Event:', 'Event Start': 'Time:'}, axis=1)

    Swimmer_Select_Pic = (validation.loc[(validation['Swimmer'] == Swimmer_Select)]['Athlete Pic URL'].unique())[0]


    session_1 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 1)])
    session_2 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 2)])
    session_3 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 3)])
    session_4 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 4)])
    session_5 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 5)])
    session_6 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 6)])
    session_7 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 7)])
    session_8 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 8)])
    session_9 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 9)])
    session_10 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 10)])
    session_11 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 11)])
    session_12 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 12)])
    session_13 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 13)])
    session_14 = pd.DataFrame(event_dataset.loc[(event_dataset['Session ID'] == 14)])
    

    swimmers_swims_entered = event_dataset.count()[0]
    swimmers_events_entered = event_dataset['Event'].nunique()
    swimmers_metres_covered = event_dataset['Distance'].sum()

    
    if session_2.count()[0] > 1:
        session_2_final_event = (float(session_2['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_2['Time:'].iloc[-1].split(':', 1)[1]))
        session_2_first_event = (float(session_2['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_2['Time:'].iloc[0].split(':', 1)[1]))
        session_2_gap = f'{int((session_2_final_event - session_2_first_event))} mins'
        session_2_gap_label = 'Session 2 Race Gap:'
    else:
        session_2_gap = ""
        session_2_gap_label = ''


    if session_4.count()[0] > 1:
        session_4_final_event = (float(session_4['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_4['Time:'].iloc[-1].split(':', 1)[1]))
        session_4_first_event = (float(session_4['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_4['Time:'].iloc[0].split(':', 1)[1]))
        session_4_gap = f'{int((session_4_final_event - session_4_first_event))} mins'
        session_4_gap_label = 'Session 4 Race Gap:'
    else:
        session_4_gap = ""
        session_4_gap_label = ''


    if session_6.count()[0] > 1:
        session_6_final_event = (float(session_6['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_6['Time:'].iloc[-1].split(':', 1)[1]))
        session_6_first_event = (float(session_6['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_6['Time:'].iloc[0].split(':', 1)[1]))
        session_6_gap = f'{int((session_6_final_event - session_6_first_event))} mins'
        session_6_gap_label = 'Session 6 Race Gap:'
    else:
        session_6_gap = ""
        session_6_gap_label = ''


    if session_8.count()[0] > 1:
        session_8_final_event = (float(session_8['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_8['Time:'].iloc[-1].split(':', 1)[1]))
        session_8_first_event = (float(session_8['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_8['Time:'].iloc[0].split(':', 1)[1]))
        session_8_gap = f'{int((session_8_final_event - session_8_first_event))} mins'
        session_8_gap_label = 'Session 8 Race Gap:'
    else:
        session_8_gap = ""
        session_8_gap_label = ''


    if session_10.count()[0] > 1:
        session_10_final_event = (float(session_10['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_10['Time:'].iloc[-1].split(':', 1)[1]))
        session_10_first_event = (float(session_10['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_10['Time:'].iloc[0].split(':', 1)[1]))
        session_10_gap = f'{int((session_10_final_event - session_10_first_event))} mins'
        session_10_gap_label = 'Session 10 Race Gap:'
    else:
        session_10_gap = ""
        session_10_gap_label = ''


    if session_12.count()[0] > 1:
        session_12_final_event = (float(session_12['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_12['Time:'].iloc[-1].split(':', 1)[1]))
        session_12_first_event = (float(session_12['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_12['Time:'].iloc[0].split(':', 1)[1]))
        session_12_gap = f'{int((session_12_final_event - session_12_first_event))} mins'
        session_12_gap_label = 'Session 12 Race Gap:'
    else:
        session_12_gap = ""
        session_12_gap_label = ''


    if session_14.count()[0] > 1:
        session_14_final_event = (float(session_14['Time:'].iloc[-1].split(':', 1)[0]) * 60) + (float(session_14['Time:'].iloc[-1].split(':', 1)[1]))
        session_14_first_event = (float(session_14['Time:'].iloc[0].split(':', 1)[0]) * 60) + (float(session_14['Time:'].iloc[0].split(':', 1)[1]))
        session_14_gap = f'{int((session_14_final_event - session_14_first_event))} mins'
        session_14_gap_label = 'Session 14 Race Gap:'
    else:
        session_14_gap = ""
        session_14_gap_label = ''



    #Setting containers

    main_overview = st.container()

    with main_overview:
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.image('https://www.britishswimming.org/media/images/BritishSwimming-OneTeam-Colour.original.png')
            st.title("British Swimming World Championships Schedule Viewer")
            st.subheader("Exploratory Event Timetable:")
    
        with col_2:
            st.image(Swimmer_Select_Pic)

        with col_3:
            st.metric('Events Entered:',str(swimmers_events_entered))
            st.metric('Potential Swims:',str(swimmers_swims_entered))
            st.metric('Potential Metres:',str(swimmers_metres_covered))

    
    st.markdown("""---""")


    body_overview = st.container()

    with body_overview:
        col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric("","23/07", "Session 1")
        session_1_new = session_1[['Event:', 'Time:']]
        session_1_new = session_1_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_1_new.set_index(session_1_new.columns[0]))
                                 
    with col_2:
        st.metric("", "24/07", "Session 3")
        session_3_new = session_3[['Event:', 'Time:']]
        session_3_new = session_3_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_3_new.set_index(session_3_new.columns[0]))
     
    with col_3:
        st.metric("", "25/07", "Session 5")
        session_5_new = session_5[['Event:', 'Time:']]
        session_5_new = session_5_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_5_new.set_index(session_5_new.columns[0]))

    with col_4:
        st.metric("", "26/07", "Session 7")
        session_7_new = session_7[['Event:', 'Time:']]
        session_7_new = session_7_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_7_new.set_index(session_7_new.columns[0]))

    with col_5:
        st.metric("", "27/07", "Session 9")
        session_9_new = session_9[['Event:', 'Time:']]
        session_9_new = session_9_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_9_new.set_index(session_9_new.columns[0]))
    
    with col_6:
        st.metric("", "28/07", "Session 11")
        session_11_new = session_11[['Event:', 'Time:']]
        session_11_new = session_11_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_11_new.set_index(session_11_new.columns[0]))

    with col_7:
        st.metric("", "29/07", "Session 13")
        session_13_new = session_13[['Event:', 'Time:']]
        session_13_new = session_13_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_13_new.set_index(session_13_new.columns[0]))


    col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric("", "", "Session 2")
        session_2_new = session_2[['Event:', 'Time:']]
        session_2_new = session_2_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_2_new.set_index(session_2_new.columns[0]))
        
    with col_2:
        st.metric("", "", "Session 4")
        session_4_new = session_4[['Event:', 'Time:']]
        session_4_new = session_4_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_4_new.set_index(session_4_new.columns[0]))
        
    with col_3:
        st.metric("", "", "Session 6")
        session_6_new = session_6[['Event:', 'Time:']]
        session_6_new = session_6_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_6_new.set_index(session_6_new.columns[0]))

    with col_4:
        st.metric("", "", "Session 8")
        session_8_new = session_8[['Event:', 'Time:']]
        session_8_new = session_8_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_8_new.set_index(session_8_new.columns[0]))

    with col_5:
        st.metric("", "", "Session 10")
        session_10_new = session_10[['Event:', 'Time:']]
        session_10_new = session_10_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_10_new.set_index(session_10_new.columns[0]))
    
    with col_6:
        st.metric("", "", "Session 12")
        session_12_new = session_12[['Event:', 'Time:']]
        session_12_new = session_12_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_12_new.set_index(session_12_new.columns[0]))

    with col_7:
        st.metric("", "", "Session 14")
        session_14_new = session_14[['Event:', 'Time:']]
        session_14_new = session_14_new.rename({'Time:': ''}, axis=1)
        st.dataframe(session_14_new.set_index(session_14_new.columns[0]))
    


    col_1, col_2, col_3, col_4, col_5, col_6, col_7 = st.columns(7)

    with col_1:
        st.metric(session_2_gap_label, session_2_gap)

    with col_2:
        st.metric(session_4_gap_label, session_4_gap)

    with col_3:
        st.metric(session_6_gap_label, session_6_gap)

    with col_4:
        st.metric(session_8_gap_label, session_8_gap)

    with col_5:
        st.metric(session_10_gap_label, session_10_gap)

    with col_6:
        st.metric(session_12_gap_label, session_12_gap)

    with col_7:
        st.metric(session_14_gap_label, session_14_gap)
        



        
if Password_Provided == password:
        if Viewer_Method == 'Swimmer View':
            Swimmer_View()
        elif Viewer_Method == 'Coach View':
            Coach_View()
        else:
            Hypothetical_View()
else:
    Access_Denied()



