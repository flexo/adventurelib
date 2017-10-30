# compile this file to javascript using
# $ transcrypt -b -n -m web.py
# then open web.html

KEYCODE_ENTER = 13 # TODO - is this the right way to do it?

class WebIO:
    def __init__(self, document):
        self._input_elem = document.getElementById('input')
        self._input_elem.addEventListener('keyup', self._on_input)
        self._output_elem = document.getElementById('output')

    def output(self, text, scroll=True):
        p = document.createElement('P')
        p.appendChild(document.createTextNode(text))
        self._output_elem.appendChild(p)
        if scroll:
            window.scrollTo(0, document.body.scrollHeight);

    def _on_input(self, event):
        if event.keyCode == KEYCODE_ENTER:
            self.output('> ' + self._input_elem.value)
            self._input_elem.value = ''
            self.output('...')

def onload():
    webio = WebIO(document)
    webio.output('this is a test')

window.onload = onload
