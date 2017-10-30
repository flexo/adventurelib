# this file is intended to be used with transcrypt

import sys
import adventurelib

console.log('web.py')
console.log(adventurelib)
console.log(adventurelib.Bag) # FIXME - this is coming up as undefined?
console.log('---')

KEYCODE_ENTER = 13 # TODO - is this the right way to do it?

class WebIO:
    def __init__(self, document):
        self._input_elem = document.getElementById('input')
        self._input_elem.addEventListener('keyup', self._on_input)
        self._output_elem = document.getElementById('output')

    def output(self, text, scroll=True):
        '''Append text to the output div "console".
        
        Each call generates a new paragraph.
        '''
        p = document.createElement('P')
        p.appendChild(document.createTextNode(text))
        self._output_elem.appendChild(p)
        if scroll:
            window.scrollTo(0, document.body.scrollHeight);

    def say(self, msg):
        '''Function to replace regular say()'''
        self.output(msg)

    def _on_input(self, event):
        if event.keyCode == KEYCODE_ENTER:
            cmd = self._input_elem.value
            self.output('> ' + cmd)
            self._input_elem.value = ''
            adventurelib._handle_command(cmd)

def onload():
    webio = WebIO(document)
    webio.output('this is a test')
    adventurelib.say = webio.say
    adventurelib.start = lambda: None

    # the user's main game module, renamed to webgamemain by adventure2web:
    import webgamemain
    console.log('test')

window.onload = onload
