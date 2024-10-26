def introspection_info(obj):
    type_obj = type(obj).__name__                                                   #Тип объекта.
    atr_obj = dir(obj)                                                              #Атрибуты объекта.
    method_obj = [method for method in atr_obj if callable(getattr(obj, method))]   #Методы объекта.
    module_obj = obj.__class__.__module__                                   #Модуль, к которому объект принадлежит.

    result = (f'type:{type_obj}\n'
              f'attributes:{atr_obj}\n'
              f'methods:{method_obj}\n'
              f'module:{module_obj}')
    return result

number_info = introspection_info(42)
print(number_info)