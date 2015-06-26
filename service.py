# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import requests
from pyquery import PyQuery

app_cnt = {
    'jinja2_env': Environment(loader = FileSystemLoader('templates'))
}

def get_advise():
    site_content = requests.get('http://www.fucking-great-advice.com').content
    site_dom = PyQuery(site_content)
    return site_dom('h2:first').html()

def app(environ, start_response):
    env = app_cnt['jinja2_env']
    response_body = env.get_template('index.html').render(advise = get_advise())

    start_response('200 OK', [])
    return [response_body.encode('utf-8')]

