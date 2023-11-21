import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_style("whitegrid")

# FUNGSI AIR POLUTION
def air_polution_df(df, option):
    df['yr'] = df['year']
    df['mo'] = df['month']
    df['dd'] = df ['day']
    df['hr'] =df['hour']
    df['PM_2.5'] = df['PM2.5']
    df['PM_10'] = df['PM10']
    df['SO_2'] = df['SO2']
    df['NO_2'] = df['NO2']
    df['CO_'] = df['CO']
    df['O_3'] = df['O3']
    air_polution_df = df[['yr', 'mo', 'dd', 'hr', 'PM_2.5', 'PM_10', 'SO_2', 'NO_2', 'CO_', 'O_3']].copy()
    air_polution_df = air_polution_df.rename(columns ={
        'yr' :'year',
        'mo' :'month',
        'dd' : 'day',
        'hr' :'hour',
        'PM_2.5' : 'PM2.5',
        'PM_10' : 'PM10',
        'SO_2'  : 'SO2',
        'NO_2'  : 'NO2',
        'CO_'  : 'CO',
        'O_3' : 'O3'})
    if (option == "1 Day"):
        air_polution_df = df.groupby(by = ['year', 'month', 'day','hour'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month', 'day','hour'], ascending = True)
        air_polution_df = air_polution_df.reset_index()
        air_polution_df['time'] = air_polution_df["hour"].astype(str) + ":00"
    elif (option == "Daily"):
        air_polution_df = df.groupby(by = ['year', 'month', 'day'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month', 'day'], ascending = True)
        air_polution_df = air_polution_df.reset_index()
        air_polution_df['time'] = air_polution_df["year"].astype(str) + "-" + air_polution_df["month"].astype(str) + "-" + air_polution_df["day"].astype(str)
    elif (option == "Monthly"):
        air_polution_df = df.groupby(by = ['year', 'month'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month'], ascending = True)
        air_polution_df = air_polution_df.reset_index()
        air_polution_df['time'] = air_polution_df["year"].astype(str) + "-" + air_polution_df["month"].astype(str)
    else:
        air_polution_df = df.groupby(by = ['year'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year'], ascending = True)
        air_polution_df = air_polution_df.reset_index()
        air_polution_df['time'] = air_polution_df["year"].astype(str)
    return air_polution_df
def airpolution_display(df):
    pm25= round(df['PM2.5'].mean(), 1)
    pm10= round(df['PM10'].mean(), 0)
    SO2= round(df['SO2'].mean(), 2)
    NO2= round(df['NO2'].mean(), 2)
    CO= round(df['CO'].mean(), 2)
    O3= round(df['O3'].mean(),2)

    with st.container():
        col1, col2, col3 = st.columns([2,1,1])
        with col1:
            if (pm25 <= 15.5):
                st.metric("PM25: " + str(pm25), value= "BAIK" )
            elif ((pm25 >= 15.6) & (pm25 <= 55.4)):
                st.metric("PM25: " + str(pm25), value= "SEDANG" )
            elif ((pm25 >= 55.5) & (pm25 <= 150.4)):
                st.metric("PM25: " + str(pm25), value= "TIDAK SEHAT" )
            elif ((pm25 >= 150.5) & (pm25 <= 250.4)):
                st.metric("PM25: " + str(pm25), value= "SANGAT TIDAK SEHAT")
            else:
                st.metric("PM25: " + str(pm25), value= "BERBAHAYA" )
        with col2:
            st.metric("SO2:", value = SO2)
        with col3:
                st.metric("NO2:", value = NO2)

    with st.container():
        col1,col2, col3 = st.columns([2,1,1])
        with col1:
            if (pm10 <= 50):
                st.metric("PM10: " + str(pm10), value= "BAIK" )
            elif ((pm10  >= 51) & (pm10 <= 150)):
                st.metric("PM10: " + str(pm10), value= "SEDANG" )
            elif ((pm10  >= 151) & (pm10  <= 350)):
                st.metric("PM10: " + str(pm10), value= "TIDAK SEHAT" )
            elif ((pm10 >= 351) & (pm10 <= 420)):
                st.metric("PM10: " + str(pm10), value= "SANGAT TIDAK SEHAT" )
            else:
                st.metric("PM10: " + str(pm10), value= "BERBAHAYA" )
        with col2:
            st.metric("CO:", value = CO)
        with col3:
            st.metric("O3:", value = O3)
def air_polution_graph(df):
    with st.expander("PM2.5"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['PM2.5'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("PM2.5", fontsize=25)
        ax.set_title("PM2.5", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("PM10"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['PM10'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("PM10", fontsize=25)
        ax.set_title("PM10", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("SO2"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['SO2'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("SO2", fontsize=25)
        ax.set_title("SO2", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("NO2"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['NO2'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("NO2", fontsize=25)
        ax.set_title("NO2", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("CO"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['CO'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("CO", fontsize=25)
        ax.set_title("CO", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("O3"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['O3'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("O3", fontsize=25)
        ax.set_title("O3", loc="center", fontsize=35)
        st.pyplot(fig)

#FUNGSI AIR PARAMETERS
def air_parameters_df(df, option):
    df['yr'] = df['year']
    df['mo'] = df['month']
    df['dd'] = df ['day']
    df['hr'] =df['hour']
    df['suhu'] = df['TEMP']
    df['tekanan'] = df['PRES']
    df['SO_2'] = df['SO2']
    df['NO_2'] = df['NO2']
    df['CO_'] = df['CO']
    df['O_3'] = df['O3']
    air_parameters_df = df[['yr', 'mo', 'dd', 'hr', 'suhu', 'tekanan']].copy()
    air_parameters_df = air_parameters_df.rename(columns ={
        'yr' :'year',
        'mo' :'month',
        'dd' : 'day',
        'hr' :'hour',
        'suhu' : 'TEMP',
        'tekanan' : 'PRES'})
    if (option == "1 Day"):
        air_parameters_df = df.groupby(by = ['year', 'month', 'day','hour'] ).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year', 'month', 'day','hour'], ascending = True)
        air_parameters_df = air_parameters_df.reset_index()
        air_parameters_df['time'] = air_parameters_df["hour"].astype(str) + ":00"
    elif (option == "Daily"):
        air_parameters_df = df.groupby(by = ['year', 'month', 'day'] ).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year', 'month', 'day'], ascending = True)
        air_parameters_df = air_parameters_df.reset_index()
        air_parameters_df['time'] = air_parameters_df["year"].astype(str) + "-" + air_parameters_df["month"].astype(str) + "-" + air_parameters_df["day"].astype(str)
    elif (option == "Monthly"):
        air_parameters_df = df.groupby(by = ['year', 'month'] ).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year', 'month'], ascending = True)
        air_parameters_df = air_parameters_df.reset_index()
        air_parameters_df['time'] = air_parameters_df["year"].astype(str) + "-" + air_parameters_df["month"].astype(str)
    else:
        air_parameters_df = df.groupby(by = ['year'] ).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year'], ascending = True)
        air_parameters_df = air_parameters_df.reset_index()
        air_parameters_df['time'] = air_parameters_df["year"].astype(str)
    return air_parameters_df
def airparameters_display(df):
    suhu= round(df['TEMP'].mean(), 2)
    tekanan= round(df['PRES'].mean(), 2)

    with st.container():
        col1, col2= st.columns(2)
        with col1:
            st.metric("TEMPERATURE:", value = str(suhu) + " °C")
        with col2:
                st.metric("PRESSURE:", value = str(tekanan) + " hPa")
def air_parameters_graph(df):
    with st.expander("Temperature"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['TEMP'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("Temperature (°C)", fontsize=25)
        ax.set_title("Temperature", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("Pressure"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['PRES'], marker='o', linewidth=2, color="#39064B")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("Pressure (hPa)", fontsize=25)
        ax.set_title("Pressure", loc="center", fontsize=35)
        st.pyplot(fig)

#Fungsi Correlation
def correlation_df(df):
    df['PM_2.5'] = df['PM2.5']
    df['PM_10'] = df['PM10']
    df['SO_2'] = df['SO2']
    df['NO_2'] = df['NO2']
    df['CO_'] = df['CO']
    df['O_3'] = df['O3']
    df['suhu'] = df['TEMP']
    df['tekanan'] =df['PRES']
    correlation_df = df[['PM_2.5', 'PM_10', 'SO_2', 'NO_2', 'CO_', 'O_3', 'suhu', 'tekanan']].copy()
    correlation_df = correlation_df.rename(columns ={
        'PM_2.5' : 'PM2.5',
        'PM_10' : 'PM10',
        'SO_2'  : 'SO2',
        'NO_2'  : 'NO2',
        'CO_'  : 'CO',
        'O_3' : 'O3',
        'suhu' : 'TEMP',
        'tekanan' : 'PRES'
    })
    return correlation_df
def correlation_suhu(df):
    pm25_suhu = round(df['PM2.5'].corr(df['TEMP'], method ="pearson"),2)
    pm10_suhu = round(df['PM10'].corr(df['TEMP'], method ="pearson"),2)
    SO2_suhu = round(df['SO2'].corr(df['TEMP'], method ="pearson"),2)
    NO2_suhu = round(df['NO2'].corr(df['TEMP'], method ="pearson"),2)
    CO_suhu = round(df['CO'].corr(df['TEMP'], method ="pearson"),2)
    O3_suhu = round(df['O3'].corr(df['TEMP'], method ="pearson"),2)
    correlation_suhu = {'parameter': ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"],
                        'values' : [pm25_suhu, pm10_suhu, SO2_suhu, NO2_suhu, CO_suhu, O3_suhu]}
    correlation_suhu_df = pd.DataFrame(correlation_suhu)
    correlation_suhu_df
def correlation_pres(df):
    pm25_pres = round(df['PM2.5'].corr(df['PRES'], method ="pearson"),2)
    pm10_pres = round(df['PM10'].corr(df['PRES'], method ="pearson"),2)
    SO2_pres = round(df['SO2'].corr(df['PRES'], method ="pearson"),2)
    NO2_pres = round(df['NO2'].corr(df['PRES'], method ="pearson"),2)
    CO_pres = round(df['CO'].corr(df['PRES'], method ="pearson"),2)
    O3_pres = round(df['O3'].corr(df['PRES'], method ="pearson"),2)
    correlation_pres = {'parameter': ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"],
                        'values' : [pm25_pres, pm10_pres, SO2_pres, NO2_pres, CO_pres, O3_pres]}
    correlation_pres_df = pd.DataFrame(correlation_pres)
    correlation_pres_df
def heatmap_graph(df):
    korelasi = df.corr(method="pearson")
    fig, ax = plt.subplots(figsize=(14, 12))
    sns.heatmap(korelasi, vmax = 1, vmin = -1, center = 0, cmap = "plasma")
    ax.tick_params(labelsize = 20)
    st.pyplot(fig)
def corr_scatter_graph(df):
    with st.expander("Air Quality VS Temperature"):
        fig1, ax1 = plt.subplots(figsize=(16, 8))
        ax1.scatter(df['TEMP'], df['PM2.5'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax1.set_xlabel("TEMPERATURE", fontsize = 20)
        ax1.set_ylabel("PM2.5", fontsize = 20)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(16, 8))
        ax2.scatter(df['TEMP'], df['PM10'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        ax2.set_xlabel("TEMPERATURE", fontsize = 20)
        ax2.set_ylabel("PM10", fontsize = 20)
        st.pyplot(fig2)

        fig3, ax3 = plt.subplots(figsize=(16, 8))
        ax3.scatter(df['TEMP'], df['SO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax3.set_xticklabels([])
        ax3.set_yticklabels([])
        ax3.set_xlabel("TEMPERATURE", fontsize = 20)
        ax3.set_ylabel("SO2", fontsize = 20)
        st.pyplot(fig3)

        fig4, ax4 = plt.subplots(figsize=(16, 8))
        ax4.scatter(df['TEMP'], df['NO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax4.set_xticklabels([])
        ax4.set_yticklabels([])
        ax4.set_xlabel("TEMPERATURE", fontsize = 20)
        ax4.set_ylabel("NO2", fontsize = 20)
        st.pyplot(fig4)

        fig5, ax5 = plt.subplots(figsize=(16, 8))
        ax5.scatter(df['TEMP'], df['CO'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax5.set_xticklabels([])
        ax5.set_yticklabels([])
        ax5.set_xlabel("TEMPERATURE", fontsize = 20)
        ax5.set_ylabel("CO", fontsize = 20)
        st.pyplot(fig5)

        fig6, ax6 = plt.subplots(figsize=(16, 8))
        ax6.scatter(df['TEMP'], df['O3'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax6.set_xticklabels([])
        ax6.set_yticklabels([])
        ax6.set_xlabel("TEMPERATURE", fontsize = 20)
        ax6.set_ylabel("O3", fontsize = 20)
        st.pyplot(fig6)

    with st.expander("Air Quality VS Pressure"):
        fig1, ax1 = plt.subplots(figsize=(16, 8))
        ax1.scatter(df['PRES'], df['PM2.5'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax1.set_xlabel("PRESSURE", fontsize = 20)
        ax1.set_ylabel("PM2.5", fontsize = 20)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(16, 8))
        ax2.scatter(df['PRES'], df['PM10'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        ax2.set_xlabel("PRESSURE", fontsize = 20)
        ax2.set_ylabel("PM10", fontsize = 20)
        st.pyplot(fig2)

        fig3, ax3 = plt.subplots(figsize=(16, 8))
        ax3.scatter(df['PRES'], df['SO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax3.set_xticklabels([])
        ax3.set_yticklabels([])
        ax3.set_xlabel("PRESSURE", fontsize = 20)
        ax3.set_ylabel("SO2", fontsize = 20)
        st.pyplot(fig3)

        fig4, ax4 = plt.subplots(figsize=(16, 8))
        ax4.scatter(df['PRES'], df['NO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax4.set_xticklabels([])
        ax4.set_yticklabels([])
        ax4.set_xlabel("PRESSURE", fontsize = 20)
        ax4.set_ylabel("NO2", fontsize = 20)
        st.pyplot(fig4)

        fig5, ax5 = plt.subplots(figsize=(16, 8))
        ax5.scatter(df['PRES'], df['CO'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax5.set_xticklabels([])
        ax5.set_yticklabels([])
        ax5.set_xlabel("PRESSURE", fontsize = 20)
        ax5.set_ylabel("CO", fontsize = 20)
        st.pyplot(fig5)

        fig6, ax6 = plt.subplots(figsize=(16, 8))
        ax6.scatter(df['PRES'], df['O3'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolor= "#ed7d53")
        ax6.set_xticklabels([])
        ax6.set_yticklabels([])
        ax6.set_xlabel("PRESSURE", fontsize = 20)
        ax6.set_ylabel("O3", fontsize = 20)
        st.pyplot(fig6)

# Fungsi Partikel by Time Span
def timespan_particle_df(df):
    df['time_span'] = df.hour.apply(lambda x: "Morning" if x >= 6 and x<=11
                                          else ("Afternoon" if x >= 12 and x<=16
                                                else ("Evening" if x >=17 and x<=23 else "Night")))
    timespan_particle_df = df.groupby(by="time_span").agg({
        "hour" : "first",
        "PM2.5":"mean",
        "PM10" :"mean"
    })
    timespan_particle_df['index'] = timespan_particle_df.hour.apply(lambda x: 0 if x >= 6 and x<=11
                                          else (1 if x >= 12 and x<=16
                                                else (2 if x >=17 and x<=23 else 3)))

    timespan_particle_df= timespan_particle_df.sort_values(by = ['index'], ascending =True)
    timespan_particle_df = timespan_particle_df.reset_index()
    timespan_particle_df = timespan_particle_df.drop(columns="index")

    return timespan_particle_df
def timespan_bar_graph(df):
    warna = ['#F59245', '#F5E926','#CE5270','#9316A0']
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
    p = sns.barplot(data= df, x= df['time_span'], y= df['PM2.5'], palette= warna, ax= ax[0], orient= 'v')
    p.tick_params(axis='y', labelsize=20)
    p.tick_params(axis='x', labelsize=20)
    p.set_xlabel(None)
    p.set_ylabel("PM2.5", fontsize = 20)

    p= sns.barplot(data= df, x = df['time_span'], y= df['PM10'], palette= warna, ax=ax[1], orient = 'v')
    p.tick_params(axis='y', labelsize=20)
    p.tick_params(axis='x', labelsize=20)
    p.set_xlabel(None)
    p.set_ylabel("PM10", fontsize = 20)

    st.pyplot(fig)

# Fungsi Wind parameters
def wind_direction_df(df):
    df["wind_direction"]= df["wd"]
    df["wind_direction2"] = df["wd"]
    wind_direction_df = df[['wind_direction', 'wind_direction2']].copy()
    wind_direction_df = wind_direction_df.groupby(by="wind_direction").agg({"wind_direction2": "count"}).sort_values(by="wind_direction2", ascending=False).reset_index()
    wind_direction_df = wind_direction_df.rename(columns = {'wind_direction2' : 'jumlah'})
    wind_direction_df['percent'] = round((wind_direction_df['jumlah'] / wind_direction_df['jumlah'].sum()) * 100, 2)
    return wind_direction_df
def wind_speed_df(df, option):
    df['yr'] = df['year']
    df['mo'] = df['month']
    df['dd'] = df ['day']
    df['hr'] =df['hour']
    df['wind_speed'] = df['WSPM']
    wind_speed_df = df[['yr', 'mo', 'dd', 'hr', 'wind_speed']].copy()
    wind_speed_df = wind_speed_df.rename(columns ={
        'yr' :'year',
        'mo' :'month',
        'dd' : 'day',
        'hr' :'hour'})
    if (option == "1 Day"):
        wind_speed_df = df.groupby(by = ['year', 'month', 'day','hour'] ).agg({
            "wind_speed" : "mean"}).sort_values(by = ['year', 'month', 'day','hour'], ascending = True)
        wind_speed_df = wind_speed_df.reset_index()
        wind_speed_df['time'] = wind_speed_df["hour"].astype(str) + ":00"
    elif (option == "Daily"):
        wind_speed_df = df.groupby(by = ['year', 'month', 'day'] ).agg({
            "wind_speed" : "mean"}).sort_values(by = ['year', 'month', 'day'], ascending = True)
        wind_speed_df = wind_speed_df.reset_index()
        wind_speed_df['time'] = wind_speed_df["year"].astype(str) + "-" + wind_speed_df["month"].astype(str) + "-" + wind_speed_df["day"].astype(str)
    elif (option == "Monthly"):
        wind_speed_df = df.groupby(by = ['year', 'month'] ).agg({
            "wind_speed" : "mean"}).sort_values(by = ['year', 'month'], ascending = True)
        wind_speed_df = wind_speed_df.reset_index()
        wind_speed_df['time'] = wind_speed_df["year"].astype(str) + "-" + wind_speed_df["month"].astype(str)
    else:
        wind_speed_df = df.groupby(by = ['year'] ).agg({
            "wind_speed" : "mean"}).sort_values(by = ['year'], ascending = True)
        wind_speed_df = wind_speed_df.reset_index()
        wind_speed_df['time'] = wind_speed_df["year"].astype(str)
    return wind_speed_df
def winddirection_barh_graph(df):
    fig, ax = plt.subplots(figsize=(16, 8))
    p = sns.barplot(data= df, x= df['percent'], y= df['wind_direction'], palette= 'plasma', ax= ax, orient= 'h')
    p.tick_params(axis='y', labelsize=20)
    p.bar_label(p.containers[0], fmt= '%.2f', fontsize = 18)
    p.set_xticklabels([])
    p.set_ylabel(None)
    p.set_xlabel("Percentage (%)", fontsize = 20)
    st.pyplot(fig)
def wind_speed_graph(df):
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(df['time'], df['wind_speed'], marker='o', linewidth=2, color="#BD1266")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
    ax.set_ylabel("Wind Speed (m/s)", fontsize=25)
    ax.set_title("Wind Speed", loc="center", fontsize=35)
    st.pyplot(fig)

# Get data
all_df = pd.read_csv("dashboard/dashboard_data.csv")
all_df.sort_values(by="date_time", inplace=True)
all_df.reset_index(inplace=True)
all_df['date_time'] = pd.to_datetime(all_df['date_time'], format='%Y-%m-%d %H:%M:%S')

#extract date_time
min_date = all_df['date_time'].min()
max_date = all_df['date_time'].max()

#MAIN
st.title("Air Quality in Aotizhongxin")
with st.sidebar:
    option = st.selectbox("Tampilkan data:", ("1 Day", "Daily", "Monthly", "Yearly"))

if (option == "1 Day") :
    # Mengambil exact date dari date_input
    with st.sidebar:
        exact_date = st.date_input(
            label='Tanggal',
            min_value= min_date,
            max_value= max_date,
            value= None,
            format = "YYYY-MM-DD"
        )
        start_time = st.time_input(
            label = "Awal" ,
            value = None,
            step = 3600
        )
        end_time = st.time_input(
            label = "Akhir" ,
            value = None,
            step = 3600
        )

    date_start = str(exact_date) + " " + str(start_time)
    date_end = str(exact_date) + " " + str(end_time)


    main_df = all_df[(all_df['date_time'].astype(str) >= date_start) &
                     (all_df['date_time'].astype(str) <= date_end)]
    air_polution = air_polution_df(main_df, option)
    air_parameters = air_parameters_df(main_df, option)

    # Visualisasi Data Air Polution
    with st.container():
        st.header("Air Polution in Aotizhongxin")
        airpolution_display(air_polution)
        air_polution_graph(air_polution)

    # Visualisasi Data Air Parameter
    with st.container():
        st.header("Air Parameters in Aotizhongxin")
        airparameters_display(air_parameters)
        air_parameters_graph(air_parameters)

    #KORELASI
    polusi_parameter = correlation_df(main_df)

    with st.container():
        st.header("Air Polution VS Air Parameters")
        with st.container():
            st.subheader("Correlation Heatmap")
            col1, col2 = st.columns([2,1])
            with col1:
                heatmap_graph(polusi_parameter)
            with col2:
                with st.expander("Air Quality VS Temperature"):
                    correlation_suhu(polusi_parameter)
                with st.expander("Air Quality VS Pressure"):
                    correlation_pres(polusi_parameter)
        with st.container():
            st.subheader("Correlation Scatter")
            corr_scatter_graph(polusi_parameter)

    #Partikel pada rentang waktu
    particle = timespan_particle_df(main_df)
    with st.container():
        st.header("Air Polution Particulate Matter in Aotizhongxin")
        timespan_bar_graph(particle)

    #Wind parameters
    wind_direction = wind_direction_df(main_df)
    wind_speed = wind_speed_df(main_df, option)

    with st.container():
        st.header("Wind Parameters in Aotizhongxin")
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                persen = wind_direction['percent'][0]
                st.metric(str(persen) + "%", wind_direction['wind_direction'][0])
            with col2:
                with st.expander("Percentage Graph"):
                    winddirection_barh_graph(wind_direction.head(5))
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                mean = round(wind_speed['wind_speed'].mean(), 2)
                st.metric("Wind speed: ", str(mean)+ " m/s")
            with col2:
                with st.expander("Wind Speed Graph"):
                    wind_speed_graph(wind_speed)

elif (option == "Daily"):
    with st.sidebar:
    # Mengambil exact date dari date_input
        start_date, end_date = st.date_input(
            label='Tanggal',
            min_value= min_date,
            max_value= max_date,
            value= [min_date, max_date]
            )

    date_start = str(start_date) + " 00:00:00"
    date_end = str(end_date) + " 23:00:00"

    main_df = all_df[(all_df['date_time'].astype(str) >= date_start) &
                     (all_df['date_time'].astype(str) <= date_end)]

    air_polution = air_polution_df(main_df, option)
    air_parameters = air_parameters_df(main_df, option)

    # Visualisasi Data Air Polution
    with st.container():
        st.header("Air Polution in Aotizhongxin")
        airpolution_display(air_polution)
        air_polution_graph(air_polution)

    # Visualisasi Data Air Parameter
    with st.container():
        st.header("Air Parameters in Aotizhongxin")
        airparameters_display(air_parameters)
        air_parameters_graph(air_parameters)

    #KORELASI
    polusi_parameter = correlation_df(main_df)
    with st.container():
        st.header("Air Polution VS Air Parameters")
        with st.container():
            st.subheader("Correlation Heatmap")
            col1, col2 = st.columns([2,1])
            with col1:
                heatmap_graph(polusi_parameter)
            with col2:
                with st.expander("Air Quality VS Temperature"):
                    correlation_suhu(polusi_parameter)
                with st.expander("Air Quality VS Pressure"):
                    correlation_pres(polusi_parameter)
        with st.container():
            st.subheader("Correlation Scatter")
            corr_scatter_graph(polusi_parameter)

    #Partikel pada rentang waktu
    particle = timespan_particle_df(main_df)
    with st.container():
        st.header("Air Polution Particulate Matter in Aotizhongxin")
        timespan_bar_graph(particle)

    #Wind Parameters
    wind_direction = wind_direction_df(main_df)
    wind_speed = wind_speed_df(main_df, option)

    with st.container():
        st.header("Wind Parameters in Aotizhongxin")
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                persen = wind_direction['percent'][0]
                st.metric(str(persen) + "%", wind_direction['wind_direction'][0])
            with col2:
                with st.expander("Percentage Graph"):
                    winddirection_barh_graph(wind_direction.head(5))
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                mean = round(wind_speed['wind_speed'].mean(), 2)
                st.metric("Wind speed: ", str(mean)+ " m/s")
            with col2:
                with st.expander("Wind Speed Graph"):
                    wind_speed_graph(wind_speed)

elif (option == "Monthly"):
    with st.sidebar:
        # Mengambil exact date dari date_input
        start_date_bulan, end_date_bulan = st.date_input(
            label='Tanggal',
            min_value= min_date,
            max_value= max_date,
            value= [min_date, max_date]
        )

    date_start = str(start_date_bulan) + " 00:00:00"
    date_end = str(end_date_bulan) + " 23:00:00"

    main_df = all_df[(all_df['date_time'].astype(str) >= date_start) &
                     (all_df['date_time'].astype(str) <= date_end)]

    air_polution = air_polution_df(main_df, option)
    air_parameters = air_parameters_df(main_df, option)

    # Visualisasi Data Air Polution
    with st.container():
        st.header("Air Polution in Aotizhongxin")
        airpolution_display(air_polution)
        air_polution_graph(air_polution)

    # Visualisasi Data Air Parameter
    with st.container():
        st.header("Air Parameters in Aotizhongxin")
        airparameters_display(air_parameters)
        air_parameters_graph(air_parameters)

    #KORELASI
    polusi_parameter = correlation_df(main_df)
    with st.container():
        st.header("Air Polution VS Air Parameters")
        with st.container():
            st.subheader("Correlation Heatmap")
            col1, col2 = st.columns([2,1])
            with col1:
                heatmap_graph(polusi_parameter)
            with col2:
                with st.expander("Air Quality VS Temperature"):
                    correlation_suhu(polusi_parameter)
                with st.expander("Air Quality VS Pressure"):
                    correlation_pres(polusi_parameter)
        with st.container():
            st.subheader("Correlation Scatter")
            corr_scatter_graph(polusi_parameter)

    #Partikel pada rentang waktu
    particle = timespan_particle_df(main_df)
    with st.container():
        st.header("Air Polution Particulate Matter in Aotizhongxin")
        timespan_bar_graph(particle)

    #Wind Parameters
    wind_direction = wind_direction_df(main_df)
    wind_speed = wind_speed_df(main_df, option)

    with st.container():
        st.header("Wind Parameters in Aotizhongxin")
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                persen = wind_direction['percent'][0]
                st.metric(str(persen) + "%", wind_direction['wind_direction'][0])
            with col2:
                with st.expander("Percentage Graph"):
                    winddirection_barh_graph(wind_direction.head(5))
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                mean = round(wind_speed['wind_speed'].mean(), 2)
                st.metric("Wind speed: ", str(mean)+ " m/s")
            with col2:
                with st.expander("Wind Speed Graph"):
                    wind_speed_graph(wind_speed)

else:
    # Mengambil exact date dari date_input
    with st.sidebar:
        start_date_tahun, end_date_tahun = st.date_input(
            label='Tanggal',
            min_value = min_date,
            max_value = max_date,
            value = [min_date, max_date]
        )

    date_start = str(start_date_tahun) + " 00:00:00"
    date_end = str(end_date_tahun) + " 23:00:00"

    main_df = all_df[(all_df['date_time'].astype(str) >= date_start) &
                     (all_df['date_time'].astype(str) <= date_end)]

    air_polution = air_polution_df(main_df, option)
    air_parameters = air_parameters_df(main_df, option)

    # Visualisasi Data Air Polution
    with st.container():
        st.header("Air Polution in Aotizhongxin")
        airpolution_display(air_polution)
        air_polution_graph(air_polution)

    # Visualisasi Data Air Parameter
    with st.container():
        st.header("Air Parameters in Aotizhongxin")
        airparameters_display(air_parameters)
        air_parameters_graph(air_parameters)

    #KORELASI
    polusi_parameter = correlation_df(main_df)

    with st.container():
        st.header("Air Polution VS Air Parameters")
        with st.container():
            st.subheader("Correlation Heatmap")
            col1, col2 = st.columns([2,1])
            with col1:
                heatmap_graph(polusi_parameter)
            with col2:
                with st.expander("Air Quality VS Temperature"):
                    correlation_suhu(polusi_parameter)
                with st.expander("Air Quality VS Pressure"):
                    correlation_pres(polusi_parameter)
        with st.container():
            st.subheader("Correlation Scatter")
            corr_scatter_graph(polusi_parameter)

    #Partikel pada rentang waktu
    particle = timespan_particle_df(main_df)
    with st.container():
        st.header("Air Polution Particulate Matter in Aotizhongxin")
        timespan_bar_graph(particle)

    #Wind Parameters
    wind_direction = wind_direction_df(main_df)
    wind_speed = wind_speed_df(main_df, option)

    with st.container():
        st.header("Wind Parameters in Aotizhongxin")
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                persen = wind_direction['percent'][0]
                st.metric(str(persen) + "%", wind_direction['wind_direction'][0])
            with col2:
                with st.expander("Percentage Graph"):
                    winddirection_barh_graph(wind_direction.head(5))
        with st.container():
            st.subheader("Wind Direction")
            col1, col2 = st.columns([1,4])
            with col1:
                mean = round(wind_speed['wind_speed'].mean(), 2)
                st.metric("Wind speed: ", str(mean)+ " m/s")
            with col2:
                with st.expander("Wind Speed Graph"):
                    wind_speed_graph(wind_speed)

