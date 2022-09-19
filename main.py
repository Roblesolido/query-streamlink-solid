#!/usr/bin/env python
from flask import Flask, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import validators
from api import get_streams

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address
)


def query_handler(args):
    """Checks and tests arguments before serving request"""
    if not args.get("streaming-ip"):
        return "You didn't give any URL."

    # for dacast, be warned we have MULTIPLE parameters. Get it if exists
    if args.get("provider"):
        valid = validators.url(args.get("streaming-ip"))
        url = args.get("streaming-ip") + "&provider=" + args.get('provider')
        return get_streams(url) if valid else "The URL you've entered is not valid."
    else:
        valid = validators.url(args.get("streaming-ip"))
        return get_streams(args.get("streaming-ip")) if valid else "The URL you've entered is not valid."

    
def query_stream(site, idx):
    """Check if the site is enabled"""
    url = ""
    if site == "twitch":
        url = "https://www.twitch.tv/" + idx
    elif site == "youtube":
        url = "https://www.youtube.com/channel/" + idx
    elif site == "youtubevideo":
        url = "https://www.youtube.com/watch?v=" + idx

    # Check for a valid address
    valid = validators.url(url)
    return get_streams(url) if valid else "The URL you've entered is not valid."


@app.route("/", methods=['GET'])
def index():
    return "This program permits you to get direct access to streams by using Streamlink.\r\nIf you have a link that " \
           "needs to be treated, from this webpage, add /iptv-query?streaming-ip= *your URL*.\r\nNote that it will " \
           "work " \
           "only on Streamlink-supported websites.\r\nEnjoy ! LaneSh4d0w. Special thanks to Keystroke for the API " \
           "usage. "


@app.route("/<site>/<idx>.<ext>")
@limiter.limit("20/minute")
@limiter.limit("1/second")
def media(site, idx, ext):
    response = query_stream(site, idx)
    if ext == "m3u":
        return response
    elif ext == "m3u8":
        return redirect(response)
    else:
        return f"Streamlink returned nothing from query {idx}, reason being {response}"


@app.route("/iptv-query", methods=['GET'])
@limiter.limit("20/minute")
@limiter.limit("1/second")
def home():
    response = query_handler(request.args)
    valid2 = validators.url(response)
    if response is None or not valid2:
        return f"Streamlink returned nothing from query {request.args.get('streaming-ip')}, reason being {response}"

    return response if request.args.get("noredirect") == "yes" else redirect(response)


@app.errorhandler(429)
def ratelimit_handler(e):
    return f"Rate limit exceeded, cannot proceed further. Here's a message from Ground Control : {e}"


# change to your likings, params are "ip", "port", "threaded"
if __name__ == '__main__':
    app.run(threaded=False, port=5000)
