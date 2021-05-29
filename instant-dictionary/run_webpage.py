import justpy as jp


from web_app.pages import Home, About
from web_app.dictionary import Dictionary


jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy()
