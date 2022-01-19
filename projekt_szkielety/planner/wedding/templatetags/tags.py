from django import template

register = template.Library()

@register.inclusion_tag('columns.html')
def get_columns_names(queryset):
    item = queryset.first()
    columns = [k for k,v in item.__dict__.items() if k != '_state' and k != 'id']
    return {'columns' : columns }



@register.inclusion_tag('wedding/table.html')
def get_table(queryset):
    item = queryset.first()
    columns = [k for k,v in item.__dict__.items() if k != '_state' and k != 'id' and k!='email_address']
    items = [item for item in queryset]
    print("*******************")
    print(items)
    print("*******************")
    add_url = item.get_add_url()
    return {'items' : items, 'columns' : columns, 'add_url':add_url}


@register.simple_tag(name='get_attribute_for_object')
def get_attribute_for_object(obj, attribute_name, *args):
    attribute = getattr(obj, attribute_name)
    return attribute

@register.simple_tag()
def get_matching_url(object):
    url = '/' + str(object)
    url = url + '_detail'
    print("**************************")
    print(type(object))
    print("**************************")
    return url