from flask import Blueprint
from models.history_model import HistoryModel
import json

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history_list():
    result = json.loads(HistoryModel.list_as_json())
    if result:
        return result

    return []
