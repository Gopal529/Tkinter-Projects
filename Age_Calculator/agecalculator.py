import datetime

class agecalculator:
    def __init__(self, day, month, year, days_in_month):
        self.day=day
        self.month=month
        self.year=year
        self.days_in_month=days_in_month
        today_date = datetime.datetime.now()
        today_day = int(today_date.strftime("%d"))
        today_month = int(today_date.strftime("%m"))
        today_year = int(today_date.strftime("%Y"))
		
        if (self.day > today_day):
            today_month = today_month - 1
            today_day = today_day + self.days_in_month


		# if birth month exceeds given month, then
		# donot count this year and add 12 to the
		# month so that we can subtract and find out
		# the difference
        if (self.month > today_month):
            today_year = today_year - 1
            today_month = today_month + 12
        self.calculated_day = today_day - self.day;
        self.calculated_month = today_month-self.month;
        self.calculated_year = today_year -self.year;
		
    def get_days(self):
	    return self.calculated_day
		
    def get_months(self):
        return self.calculated_month
		
    def get_years(self):
        return self.calculated_year
