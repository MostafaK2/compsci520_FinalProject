from geopy.geocoders import Nominatim

def get_details(src_point, dest_point):
    geolocator = Nominatim(user_agent="EleNa-server")
    location_src = geolocator.reverse(str(src_point[1]) + ", " + str(src_point[0]))
    location_dest = geolocator.reverse(str(dest_point[1]) + ", " + str(dest_point[0]))
    src_country = location_src.raw['address']['country']
    dest_country = location_dest.raw['address']['country']
    src_state = location_src.raw['address']['state']
    dest_state = location_dest.raw['address']['state']
    # print(location_dest.raw['address'], location_src.raw['address'])
    if ("town" in location_src.raw['address'].keys()):
        src_city = location_src.raw['address']['town']
    else:
        src_city = location_src.raw['address']['city']

    if ("town" in location_dest.raw['address'].keys()):
        dest_city = location_dest.raw['address']['town']
    else:
        dest_city = location_dest.raw['address']['city']
    print(src_city, dest_city, src_state, dest_state, src_country, dest_country)

    if (src_country != dest_country or src_state != dest_state or src_city != dest_city):
        return "", "", ""
    else:
        return src_city, src_state, src_country