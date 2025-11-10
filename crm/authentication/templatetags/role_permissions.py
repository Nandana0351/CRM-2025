


from django.template import Library

register =Library()


@register.simple_tag
def display_name(name):

    return name.upper()



#  {% display_name 'Nandana Unni' as name %} templatetags using in base.html


@register.simple_tag

def check_roles(request,roles):

    roles = roles.split(',')

    if request.user.is_authenticated and request.user.role in roles :

        return True
    
    return False

