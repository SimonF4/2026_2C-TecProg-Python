"""
Ejercicio 7 - Zona Horaria Internacional
Crea un programa 
que muestre la fecha y hora actual 
    en 3 zonas horarias distintas:
            Buenos Aires, Argentina (America/Argentina/Buenos_Aires)
            Nueva York, EE.UU. (America/New_York)
            Tokio, Japón (Asia/Tokyo)

Pista: Usa el módulo pytz para asignar zonas horarias.

"""

import datetime
# pip install pytz : En consola, para instalar el pytz.
import pytz

# print(pytz.all_timezones)

dt = datetime.now(pytz.timezone('Asia/Tokyo'))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h

# TESTING:
# TEST 01: ERROR. No tiene el atributo .now(). SOLUCION: agregar el "from datetime" al import



