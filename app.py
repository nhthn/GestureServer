import common
import flask

app = flask.Flask("gesture")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/app.js")
def app_js():
    response = flask.make_response(
        flask.render_template(
            "app.js",
            ip_address=common.PRIVATE_IP_ADDRESS,
            websockets_port=common.WEBSOCKETS_PORT,
        )
    )
    response.headers["Content-type"] = "text/javascript; charset=utf-8"
    return response
