from datetime import datetime, timedelta
import time

from datetime import datetime

from dateutil.relativedelta import relativedelta

# print(datetime.datetime.now())

# print(datetime.datetime.now().date())

# date_string = "Feb 25 2020 4:20PM"

# datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
# print(datetime_object)

# given_date = datetime(2020, 2, 25)

# days_to_sub = 7
# res_date = given_date - timedelta(days=days_to_sub)
# print(res_date)

# print(given_date.strftime('%A %w %d %Y'))

# print(given_date.strftime('%A'))

# given_date = datetime(2020, 3, 22, 10, 0, 0)


# res_date = given_date + timedelta(days=7, hours=12)
# print(res_date)

# time_in_ms = int(round(time.time()*1000))
# print(time_in_ms)

# given_date = datetime(2020, 2, 25).date()

# months_to_add = 4
# new = given_date + relativedelta(months=+months_to_add)
# print(new)       

# from datetime import datetime

# from dateutil.relativedelta import relativedelta

# # 2020-02-25
# given_date = datetime(2020, 2, 25).date()

# months_to_add = 4
# new_date = given_date + relativedelta(months=+ months_to_add)
# print(new_date)

date_1 = datetime(2020, 2, 25).date()
date_2 = datetime(2020, 9, 17).date()

diff = date_2 - date_1
print(diff)