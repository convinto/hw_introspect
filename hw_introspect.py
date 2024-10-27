def introspection_info(obj):
    type_obj = type(obj).__name__                                       # Тип объекта
    attributes = list(obj.__class__.__dict__.keys())                    # Атрибуты объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]  # Методы объекта
    module_obj = obj.__class__.__module__                               # Модуль, к которому объект принадлежит

    result = (
        f"Тип объекта: {type_obj}\n"
        f"Атрибуты объекта: {', '.join(attributes)}\n"
        f"Методы объекта: {', '.join(methods)}\n"
        f"Модуль: {module_obj}"
    )

    return result


number_info = introspection_info(42)
print(number_info)