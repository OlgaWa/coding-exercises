import justpy as jp
import definition


class Dictionary:

    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-purple-300 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-4")
        jp.Div(a=div, text="Find out what's the meaning "
                           "of the word of the phrase that "
                           "you\'re typing right now!",
               classes="text-lg m-4")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-4 p-4 text-lg border border-2 h-40 border-purple-900")

        input_box = jp.Input(a=input_div, placeholder="Type in a word", outputdiv=output_div,
                             classes="m-2 bg-purple-100 border-2 border-purple-900 "
                                     "rounded w-64 focus:bg-white "
                                     "focus:border-purple-400 py-2 px-4")
        input_box.on("input", cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
