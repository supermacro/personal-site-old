# -*- coding: utf-8 -*- #

# custom jinja filters
# http://jinja.pocoo.org/docs/2.10/api/#custom-filters

def datetimeformat(value, abbreviate_month=False):
    month_formatter = '%B'

    if abbreviate_month:
        month_formatter = '%b'

    month_string = value.strftime(month_formatter)

    return "{0} {1}, {2}".format(month_string, value.day, value.year) 


def tagsort(tags):
    """
    sort a list of (tag, article) tuples

    sorting is based on the most recent article per tag (descending)
    """

    sorting_func = lambda tag_tuple: sorted(tag_tuple[1], key=lambda article: article.date, reverse=True)[0].date

    sorted_tags = sorted(tags, key=sorting_func, reverse=True)

    return sorted_tags
