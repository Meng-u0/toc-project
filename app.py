import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '507403984:AAFgB7sXxFM-qND0td_y5pBN-F4jxpv9azM'
WEBHOOK_URL = 'https://cd79d809.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token='507403984:AAFgB7sXxFM-qND0td_y5pBN-F4jxpv9azM')
machine = TocMachine(
    states=[
        'distance',
        'price1',
        'price2',
        'category1',
        'category2',
        'category3',
        'category4',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8'
    ],
    transitions=[
        {
            'trigger':'advance',
            'source':'distance',
            'dest':'price1',
            'conditions': 'is_going_to_price1'
        },
        {
            'trigger':'advance',
            'source':'distance',
            'dest':'price2',
            'conditions': 'is_going_to_price2'
        },
        {
            'trigger':'advance',
            'source':'price1',
            'dest':'category1',
            'conditions': 'is_going_to_category1'
        },
        {
            'trigger':'advance',
            'source':'price1',
            'dest':'category2',
            'conditions': 'is_going_to_category2'
        },
        {
            'trigger':'advance',
            'source':'price2',
            'dest':'category3',
            'conditions': 'is_going_to_category3'
        },
        {
            'trigger':'advance',
            'source':'price2',
            'dest':'category4',
            'conditions': 'is_going_to_category4'
        },
        {
            'trigger':'advance',
            'source':'category1',
            'dest':'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger':'advance',
            'source':'category1',
            'dest':'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger':'advance',
            'source':'category2',
            'dest':'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger':'advance',
            'source':'category2',
            'dest':'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger':'advance',
            'source':'category3',
            'dest':'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger':'advance',
            'source':'category3',
            'dest':'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger':'advance',
            'source':'category4',
            'dest':'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger':'advance',
            'source':'category4',
            'dest':'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger':'advance',
            'source':[
                'price1',
                'price2',
                'category1',
                'category2',
                'category3',
                'category4',
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state6',
                'state7',
                'state8'
            ],
            'dest':'distance',
            'conditions': 'is_going_to_distance'
        }
    ],
    initial='distance',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook("https://cd79d809.ngrok.io/hook")
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format("https://cd79d809.ngrok.io/hook"))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
        byte_io = BytesIO()
        machine.graph.draw(byte_io, prog='dot', format='png')
        byte_io.seek(0)
        return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

if __name__ == "__main__":
    _set_webhook()
    app.run()