def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday
have_umbrella = True
rain_level = 0.0
have_hood  = True
is_workday = True

actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)