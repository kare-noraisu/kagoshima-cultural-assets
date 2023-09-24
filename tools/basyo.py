from geopy.geocoders import Nominatim
import csv
geolocator=Nominatim(user_agent="myGeocoder")
csv_file= open("output.csv","r",encoding='utf-8-sig')
f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="\r\n",quotechar='"',skipinitialspace=True)
csv_file.close
locations=list(f)
print(locations[0])
with open('places.csv','w',encoding="utf-8-sig",newline="") as f:
    writer=csv.writer(f)
    for location in locations:
        location_name=f"鹿児島市{location[0]}"
        try:
            geo_location=geolocator.geocode(location_name)
            if geo_location is not None:
                writer.writerow([location_name,geo_location.latitude,geo_location.longitude])
            else:
                writer.writerow([location_name,'Not Found','Not Found'])
        except Exception as e:
            print(f"Error:{e}")