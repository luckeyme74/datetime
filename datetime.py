class Datetime(object):
    """represents today's date"""
d = Datetime()
d.year = 2016
d.month = 11
d.day = 10

def print_date(d):
    print '%.2d/%.2d/%.2d' % (d.day, d.month, d.year)

print_date(d)

