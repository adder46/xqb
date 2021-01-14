import pendulum

from django import template

register = template.Library()


@register.simple_tag
def note_ago(user, note):
    now = pendulum.now().in_timezone(user.profile.timezone)
    note_date = pendulum.instance(note.added_on).in_timezone(user.profile.timezone)
    seconds_passed = (now - note_date).total_seconds()
    days_passed = seconds_passed / 86400
    diff = now.subtract(days=days_passed).diff_for_humans()
    for k, v in {
        'a few seconds ago': '0s',
        ' seconds ago': 's',
        ' minute ago': 'm',
        ' minutes ago': 'm',
        ' hour ago': 'h',
        ' hours ago': 'h',
        ' day ago': 'd',
        ' days ago': 'd',
        ' week ago': 'w',
        ' weeks ago': 'w',
        ' month ago': 'M',
        ' months ago': 'M',
        ' year ago': 'y',
        ' years ago': 'y',
    }.items():
        diff = diff.replace(k, v)
    return diff
