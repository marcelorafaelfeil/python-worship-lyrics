from screens.preferences.forms import WebSocketForm, HTTPForm, GeneralForm

advanced_options = ({
    'widget': GeneralForm,
    'label': 'Geral'
}, {
    'widget': WebSocketForm,
    'label': 'WebSocket'
}, {
    'widget': HTTPForm,
    'label': 'HTTP'
})

options = advanced_options

default_option = advanced_options[0]
