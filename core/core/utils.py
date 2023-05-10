import geoip2.database

def get_country_by_ip(ip_address):
    reader = geoip2.database.Reader('geoip/GeoLite2-Country.mmdb')
    try:
        response = reader.country(ip_address)
        return response.country.iso_code
    except geoip2.errors.AddressNotFoundError:
        return None
