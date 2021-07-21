def add_time(start, duration, starting_day=''):
    time_converter = TimeConverter(start, duration, starting_day)

    time_converter.convert_input_to_values()
    time_converter.calc_tot_min()
    time_converter.calc_new_time_values()
    new_time_strings = time_converter.format_new_values_to_strings()

    return '{}:{} {}{}{}'.format(*new_time_strings)


class TimeConverter:
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def __init__(self, start, duration, starting_day):
        self.start = start
        self.duration = duration
        self.starting_day = starting_day

        self.cur_h = 0
        self.cur_min = 0
        self.additional_h = 0
        self.additional_min = 0
        self.am_pm_additional_h = 0

        self.tot_min = 0

        self.new_h = 0
        self.new_min = 0
        self.pm_time = None
        self.new_day = 0

    def convert_input_to_values(self):
        cur_time, cur_am_pm = self.start.split()
        self.cur_h, self.cur_min = [int(time) for time in cur_time.split(':')]
        self.additional_h, self.additional_min = [int(time) for time in self.duration.split(':')]
        self.am_pm_additional_h = 0 if cur_am_pm == 'AM' else 12

    def calc_tot_min(self):
        self.cur_h += self.additional_h + self.am_pm_additional_h
        self.cur_min += self.additional_min
        self.tot_min = self.cur_min + self.cur_h * 60

    def calc_new_time_values(self):
        self.new_h = (self.tot_min // 60) % 12
        self.new_min = self.tot_min % 60
        self.pm_time = ((self.tot_min // 60) // 12) % 2
        self.new_day = (self.tot_min // 60) // 24

    def get_new_day_str(self):
        new_day_str = ''
        if self.new_day == 1:
            new_day_str = ' (next day)'
        elif self.new_day > 1:
            new_day_str = f' ({self.new_day} days later)'

        return new_day_str

    def get_new_week_day_str(self):
        new_week_day_str = ''
        if self.starting_day.lower() in self.week_days:
            cur_week_day = self.week_days.index(self.starting_day.lower())
            new_week_day_idx = (self.new_day + cur_week_day) % 7
            new_week_day = self.week_days[new_week_day_idx].title()
            new_week_day_str = f', {new_week_day}'

        return new_week_day_str

    def format_new_values_to_strings(self):
        new_h_str = '12' if self.new_h == 0 else str(self.new_h)
        new_min_str = f'{self.new_min:02d}'
        new_am_pm_str = 'PM' if self.pm_time else 'AM'
        new_week_day_str = self.get_new_week_day_str()
        new_day_str = self.get_new_day_str()

        return new_h_str, new_min_str, new_am_pm_str, new_week_day_str, new_day_str
