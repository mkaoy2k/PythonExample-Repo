import datetime
import pytz

# Naive
d = datetime.date(2001, 9, 11)
print('datetime.date(2001, 9, 11):\t', d)
print('\t Year(2001, 9, 11):\t', d.year)
print('\t Month(2001, 9, 11):\t', d.month)
print('\t Day(2001, 9, 11):\t', d.day)
print()

tday = datetime.date.today()
print("Today's date: \t", tday)
print('\t day:\t', tday.day)

# weekday() - Monday is 0 and Sunday is 6
print('\t weekday(Monday is 0 and Sunday is 6):\t', tday.weekday())

# isoweekday() - Monday is 1 and Sunday is 7
print('\t iso weekday(Monday is 1 and Sunday is 7):\t', tday.isoweekday())
print()

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(days=7, hours=12)

print('7 days and 12 hours from today:\t', tday + tdelta)

bday = datetime.date(tday.year, 12, 20)
till_bday = bday - tday

print('{0} days left till DP birthday'.format(till_bday.days))
print('{0:,.2f} seconds left till DP birthday'.format(till_bday.total_seconds()))
print()

t = datetime.time(9, 30, 45, 100000)
print('The datetime.time(9, 30, 45, 100000):\t', t)

# print( ttime)
# print('Current hour:\t', ttime.hour)

dt = datetime.datetime.today()
dtnow = datetime.datetime.now()
# print(dir(datetime.datetime))
print('datetime.datetime.today():\t', dt)
print('datetime.datetime.now():\t', dtnow)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print('datetime.datetime.now(tz=pytz.UTC):\t', dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print('.utcnow().replace(tzinfo=pytz.UTC):\t', dt_utcnow2)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(".astimezone(pytz.timezone('US/Mountain')):\t", dt_mtn)

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

print('Time zone aware: Mountain time:\t', dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print('Time zone aware: Eastern time:\t', dt_east)


# strftime - Datetime to String
print('strftime - Datetime to String:\t', dt_mtn.strftime('%B %d, %Y'))

# strptime - String to Datetime
dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print('strptime - String to Datetime:\t', dt)
