import datetime as dt

from django.conf import settings


def registration_year_range(year_delta=0):
    now = dt.datetime.now().date()

    if now.month < settings.REGISTRATION_FIRST_MONTH:
        # We are between the start of year and the start of the school year
        lyear = now.year - 1
    else:
        # We are between the start of the school year and the end of the year
        lyear = now.year
    lyear += year_delta

    ldate = dt.date(
        year=lyear,
        month=settings.REGISTRATION_FIRST_MONTH,
        day=settings.REGISTRATION_FIRST_DAY
    )
    hdate = dt.date(lyear+1, ldate.month, ldate.day) + dt.timedelta(days=-1)

    return ldate, hdate
