import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Photon
from streamlit_js_eval import get_geolocation
def main():
    df=pd.read_csv('file.csv')
    st.set_page_config(layout="wide")
    page=st.sidebar.selectbox("Choose a page",["Database View","Map View","about"])
    if page == "Database View":
        st.header("Database View")
        col1,col2,col3=st.columns(3)
        with col1:
            sort_option=st.selectbox('Sort by',df.columns)
            df=df.sort_values(sort_option)
        with col2:
            filter_column=st.selectbox('Filter column:',df.columns)
            unique_values_in_column=df[filter_column].unique()
        with col3:
            selected_value=st.selectbox('Filter by:',unique_values_in_column)
            df=df[df[filter_column]==selected_value]
        st.dataframe(df,use_container_width=True)
    elif page == "Map View":
        st.header("Map View")
        geolocator=Photon(user_agent="geoapiExerclses")
        loc=get_geolocation()
        if loc is not None:
            loc=loc['coords']
            map=folium.Map(location=[loc["latitude"],loc["longitude"]],zoom_start=15)
        else:
            map=folium.Map(location=[31.5965,130.5571],zoom_start=10)
        df=pd.read_csv('data.csv')
        for idx,row in df.iterrows():
            if row["Latitude"]!="Not Found":
                folium.Marker([row["Latitude"],row["Longitude"]],popup=row['名称'],icon=folium.Icon(color='black',icon="arrow-down",icon_color="white")).add_to(map)
        if loc is not None:
            folium.Marker([loc["latitude"],loc["longitude"]],
                          popup="You are here!",
                          icon=folium.Icon(color='red')).add_to(map)
            st.components.v1.html(folium.Figure().add_child(map).render(), height=500)
    elif page == "about":
        st.header("about")
        multi = '''このページは鹿児島市の文化遺産を二つの見方で調べられます。
        また、自分のいる座標により近くにある文化財を見つけられます。

        下記の鹿児島市のオープンデータを使用しています。
        https://www.city.kagoshima.lg.jp/ict/opendata.html

        pythonのライブラリであるstreamlitを使って作りました。
        '''
        st.markdown(multi)
        #for idx,row in df.iterrows():
            #location=geolocator.geocode(row['所在地等'])
            #if location:
                #folium.Marker([location.latitude,location.longitude],popup=row['名称']).add_to(map)
if __name__=="__main__":
    main()
