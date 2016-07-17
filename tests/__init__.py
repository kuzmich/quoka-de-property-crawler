# -*- coding: utf-8 -*-
import os
from urllib.request import urlopen

from scrapy.http import Request, Response, HtmlResponse
from scrapy.item import Item

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


def get_testdata(*paths):
    """Return content of data file"""
    path = os.path.join(DATA_DIR, *paths)
    try:
        return open(path, 'rb').read()
    except Exception:
        pass

def get_testurl(url):
    """Return content of given url"""
    try:
        return urlopen(url).read()
    except Exception:
        pass

def make_response(url, body=None, meta=None, req_args=None, **resp_args):
    def content_type(url):
        ext = os.path.splitext(url)[1].strip('.')
        if ext in ['html']:
            return 'text/html'
        elif ext in ['jpg', 'png']:
            return 'image/jpeg'
        else:
            return 'text/html'

    headers = {'Content-Type': content_type(url)}

    if body:
        #body = get_testdata(body) or get_testurl(body) or body
        body = get_testdata(body) or body
        response = HtmlResponse(url, headers=headers, body=body, **resp_args)
    else:
        response = Response(url, headers=headers, **resp_args)

    request = Request(url, meta=meta, **(req_args or {}))
    response.request = request

    return response


requests_only = lambda result: isinstance(result, Request)
items_only = lambda result: isinstance(result, (Item, dict))
urls_only = lambda request: request.url
