from sqlalchemy.inspection import inspect
import json
from decimal import Decimal
from datetime import date
from flask import make_response, jsonify
from sqlalchemy.ext.declarative import DeclarativeMeta


def custom_error(message, status_code): 
    return make_response(jsonify(message), status_code)



class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


#-------------------------------------------------------------------------------------- JSON Encoders ----------------------------------------------------------
# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o.__class__, DeclarativeMeta):
#             data = {}
#             fields = o.__json__() if hasattr(o, '__json__') else dir(o)
#             for field in [f for f in fields if not f.startswith('_') and f not in ['metadata', 'query', 'query_class']]:
#                 value = o.__getattribute__(field)
#                 try:
#                     json.dumps(value)
#                     data[field] = value
#                 except TypeError:
#                     data[field] = None
#             return data
#         return json.JSONEncoder.default(self, o)






# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, o):
#         # check if object `o` is of custom declared model instance
#         if isinstance(o.__class__, DeclarativeMeta):
#             data = {}
#             fields = o.__json__() if hasattr(o, '__json__') else dir(o)
#             for field in [f for f in fields if not f.startswith('_') and
#                           f not in ['metadata', 'query', 'query_class']]:
#                 value = o.__getattribute__(field)
#                 try:
#                     if json.dumps(value):
#                         data[field] = value
#                 except TypeError:
#                     data[field] = None
#             return data
#         # check if object `o` is of Decimal instance
#         elif isinstance(o, Decimal):
#             return o.to_eng_string()
#         # check if object `o` is of date instance
#         elif isinstance(o, date):
#             return o.isoformat()
#         # rest of objects are handled by default JSONEncoder like 'Datetime', 
#         # 'UUID', 'Markdown' and various others
#         return json.JSONEncoder.default(self, o)







# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, tuple):
#             data = {}
#             for obj in o:
#                 data.update(self.parse_sqlalchemy_object(obj))
#             return data
#         if isinstance(o.__class__, DeclarativeMeta):
#             return self.parse_sqlalchemy_object(o)
#         return json.JSONEncoder.default(self, o)

#     def parse_sqlalchemy_object(self, o):
#         data = {}
#         fields = o.__json__() if hasattr(o, '__json__') else dir(o)
#         for field in [f for f in fields if not f.startswith('_') and f not in ['metadata', 'query', 'query_class', 'registry']]:
#             value = o.__getattribute__(field)
#             try:
#                 json.dumps(value)
#                 data[field] = value
#             except TypeError:
#                 data[field] = None
#         return data





#-------------------------------------------------------------------------------------- Dynamic Filter ----------------------------------------------------------

# def get_filter_by_args(instance,dic_args: dict):
#     filters = []
#     for key, value in dic_args.items():  # type: str, any
#         if key.endswith('___min'):
#             key = key[:-6]
#             filters.append(getattr(instance, key) > value)
#         elif key.endswith('___max'):
#             key = key[:-6]
#             filters.append(getattr(instance, key) < value)
#         elif key.endswith('__min'):
#             key = key[:-5]
#             filters.append(getattr(instance, key) >= value)
#         elif key.endswith('__max'):
#             key = key[:-5]
#             filters.append(getattr(instance, key) <= value)
#         else:
#             filters.append(getattr(instance, key) == value)
#     return filters


    # dic_args = {
    #     'id':user_id,
    #     'username': username,
    # }
    # filters = get_filter_by_args(User,dic_args)