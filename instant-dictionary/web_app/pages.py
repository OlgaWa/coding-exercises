import justpy as jp
from web_app import layout
from web_app import abstract


class Home(abstract.Page):

    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-purple-300 h-screen p-4")
        jp.Div(a=div, text="Home", classes="text-4xl m-4")
        jp.Div(a=div, text="Welcome to the Instant Dictionary App",
               classes="text-lg m-4")
        return wp


class About(abstract.Page):

    path = "/about"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-purple-300 h-screen p-4")
        jp.Div(a=div, text="About", classes="text-4xl m-4")
        jp.Div(a=div, text="This is the Instant Dictionary App",
               classes="text-lg m-4")
        return wp
