import pendulum

now = pendulum.now()

print(now.to_date_string())
# 2020-01-27

print(now.to_time_string())
# 15:06:14

print(now.to_datetime_string())
# 2020-01-27 15:06:14

print(now.to_day_datetime_string())
# Mon, Jan 27, 2020 3:06 PM

print(now.to_formatted_date_string())
# Jan 27, 2020

print(now.to_iso8601_string())
# 2020-01-27T15:06:14.051517+05:30

############################

print(now.hour)


print(pendulum.today())
print(pendulum.tomorrow())
print(pendulum.yesterday())

############################

pendulum.from_format('1975-05-21 22', 'YYYY-MM-DD HH')

############################

# 3 hours ago
print(now.subtract(hours=3).diff_for_humans())

# dans 1 an
dt.diff_for_humans(locale='fr')

#############################

first = pendulum.datetime(2012, 9, 5, 23, 26, 11, 0, tz='America/Toronto')
second = pendulum.datetime(2012, 9, 5, 20, 26, 11, 0, tz='America/Vancouver')

first == second
True
first != second
False
first > second
False
first >= second
True
first < second
False
first <= second

##############################