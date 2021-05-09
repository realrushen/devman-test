from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from sheet import load_wines

DEBUG = False

BIRTH_DATE = (1920, 1, 1)
TEMPLATE_FILE = 'template.html'
SHEET_FILE = 'wine3.xlsx'
TAB_NAME = 'Лист1'
CATEGORIES_WITHOUT_GRAPE_SORT = ['Напитки']

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template(TEMPLATE_FILE)

company_age = date.today().year - date(*BIRTH_DATE).year
wines = load_wines(SHEET_FILE, TAB_NAME)

rendered_page = template.render(
    company_age=company_age,
    wines=wines,
    no_sort=CATEGORIES_WITHOUT_GRAPE_SORT
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

if not DEBUG:
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
