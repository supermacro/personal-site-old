# -*- coding: utf-8 -*- #

# custom jinja filters
# http://jinja.pocoo.org/docs/2.10/api/#custom-filters

def datetimeformat(value):
    return "{0} {1}, {2}".format(value.strftime('%B'), value.day, value.year) 
