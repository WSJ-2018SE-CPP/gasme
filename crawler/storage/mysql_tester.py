from mysql import MySQLStorage

x = MySQLStorage()

d = dict(
    address='0 Bartlett Ave, Adelanto, CA 92301',
    brand='Chevron Adelanto',
    lat='34.579504299999996',
    lon='-117.4129399',
    price_1=None,
    price_2=None,
    price_3=None)

x.store_data(data=[d])

