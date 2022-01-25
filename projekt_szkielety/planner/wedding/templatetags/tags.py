from django import template

register = template.Library()


labels = {'accomodation' : 'Nocleg','guest_capacity': 'ilosc gosci', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki',
         'importance' : 'Poziom Istotnosci',  'services' : 'Uslugi', 'quantity' : 'Ilosc', 'type' : 'Typ', 'approved':'status' }


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
    column_labels = []
    for idx, key in enumerate(columns):
        if key in labels.keys():
            column_labels.append(labels[key])
    print("*******************")
    print(items)
    print("*******************")
    print("********COLUMNS***********")
    print(columns)
    print("*******************")
    print("********COLUMNS LABELS***********")
    print(column_labels)
    print("*******************")
    add_url = item.get_add_url()
    return {'items' : items, 'columns' : columns,'column_labels': column_labels ,'add_url':add_url}


@register.inclusion_tag('wedding/detail.html')
def get_details(object):
    item = object
    keys = [k for k,v in item.__dict__.items() if k != '_state' and k != 'id']
    values = [v for k,v in item.__dict__.items() if k != '_state' and k != 'id']
    object_list = zip(keys,values)

    for idx, key in enumerate(keys):
        if key in labels.keys():
            keys[idx] = labels[key]
    print("*******************")
    print("KEYS")
    print(keys)
    print("*******************")
    print("VALUES")
    print(values)
    print("*******************")
    print("OBJECT LIST")
    print(object_list)
    print("*******************")
    name = item.name
    update_url = item.get_update_url()
    return { 'object_list': object_list, 'update_url': update_url, 'name':name}



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