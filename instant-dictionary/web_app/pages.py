import justpy as jp


class Home:

    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-purple-300 h-screen")
        jp.Div(a=div, text="Home", classes="text-4xl m-4")
        jp.Div(a=div, text="""
        Welcome to the Instant Dictionary App""",
               classes="text-lg m-4")
        return wp


class About:

    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-purple-300 h-screen")
        jp.Div(a=div, text="About", classes="text-4xl m-4")
        jp.Div(a=div, text="""
        This is the Instant Dictionary App""",
               classes="text-lg m-4")
        return wp
