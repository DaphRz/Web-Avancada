from flask import Blueprint

main = Blueprint('main',__name__)  # end point

from app.main import routes  #noqa  - ignorar essa linha na checagem