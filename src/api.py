from flask import Flask, render_template
import config

app = Flask(__name__)

@app.route('/forward', methods=['POST'])
def forwardCall():
    return render_template('forward_call.xml')

app.run(host = config.CONFIG['host'], port = config.CONFIG['port'])
