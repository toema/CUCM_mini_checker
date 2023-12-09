from ciscoaxl import axl

cucm=axl(username='axlUser20',password='Titos20',cucm='10.250.202.11',cucm_version='12.5')
try:
    device=cucm.get_phone(uuid='cbabdf55-0350-6b8b-f22b-4e17d9d8e4d')
    print(device)

except:
    print('error')