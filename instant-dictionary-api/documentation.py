import justpy as jp


class Doc:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-purple-300 h-screen p-4")
        jp.Div(a=div, text="Instant Dictionary API",
               classes="text-4xl m-4")
        jp.Div(a=div, text="Get definition of the word:",
               classes="text-lg m-4")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=rain", classes="m-4")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "rain", 
        "definition": ["Precipitation in the form of liquid water 
        drops with diameters greater than 0.5 millimetres.", 
        "To fall from the clouds in drops of water."]}""",
               classes="text-purple-700 m-4 font-medium")

        return wp
