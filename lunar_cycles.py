from datetime import datetime
from astral import moon

def get_moon_phase():

    phase = moon.phase(datetime.now())

    if phase < 7:
        return "luna creciente"

    elif phase < 14:
        return "luna llena"

    elif phase < 21:
        return "luna menguante"

    else:
        return "luna nueva"
