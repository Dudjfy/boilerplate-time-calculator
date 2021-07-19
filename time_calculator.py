def add_time(start, duration, starting_day=''):
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    cur_min = (int(start.split()[0].split(':')[0]) + (0 if start.split()[1] == 'AM' else 12)) * 60 + int(start.split()[0].split(':')[1])
    next_min = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
    cur_min += next_min

    # print(cur_min, cur_min // 60, cur_min % 60)
    # print(new_min, new_min // 60, new_min % 60)

    new_h = 12 if (cur_min // 60) % 12 == 0 else (cur_min // 60) % 12
    new_min = cur_min % 60
    new_am_pm = 'AM' if ((cur_min // 60) // 12) % 2 == 0 else 'PM'
    new_day = (cur_min // 60) // 24
    new_day_msg = '' if new_day < 1 else (' (next day)' if new_day == 1 else f' ({new_day} days later)')
    new_week_day_msg = week_days[new_day % 7 + week_days.index(starting_day.lower())] if starting_day.lower() in week_days else ''

    new_time = '{}:{:02d} {}{}{}'.format(new_h, new_min, new_am_pm, new_week_day_msg, new_day_msg)

    return new_time