import justpy as jp
import inspect

from web_app import abstract
from web_app.pages import Home, About
from web_app.dictionary import Dictionary


imports = list(globals().values())

for item in imports:
    if inspect.isclass(item):
        if issubclass(item, abstract.Page) and item is not abstract.Page:
            jp.Route(item.path, item.serve)


jp.justpy()
