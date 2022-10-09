from screens.preferences.forms import WebSocketForm, HTTPForm

advanced_options = ({
    'widget': WebSocketForm,
    'label': 'WebSocket'
}, {
    'widget': HTTPForm,
    'label': 'HTTP'
})

options = advanced_options

default_option = advanced_options[0]
