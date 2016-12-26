from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Import at the end to avoid circular references, views need app variable from this package
# noinspection PyUnresolvedReferences
from app import views
