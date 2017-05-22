# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter
def status_ball(color):
    if 'anime' in color:
        sfx = 'gif'
    else:
        sfx = 'png'
    return "images/{0}.{1}".format(color, sfx)

@register.filter
def valid_point(question):
    q = question
    vp = q.point
    if q.answer:
        vp = 0
    elif q.hint1 and q.hint2:
        vp = q.point * 0.5
    elif q.hint1 and not q.hint2:
        vp = q.point * 0.8
    if q.point == vp:
        result = str(q.point)
    else:
        result = "{}→{}".format(q.point, int(vp))
    return result
