from django import template
from django.utils.html import format_html
register=template.Library()

@register.simple_tag
def circle_tag(curr_page,loop_page):
    offset=abs(curr_page-loop_page)
    if offset<10:
        if curr_page==loop_page:
            page_ele='<li class="active"><a href="{0}">{1}</a></li>'.format(loop_page,loop_page)
        else:
            page_ele='<li><a href="%s">%s</a></li>'%(loop_page,loop_page)

        return format_html(page_ele)
    else:
        return "..."