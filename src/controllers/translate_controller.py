from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()

    if request.method == "GET":
        return render_template(
            "index.html", languages=languages, translated="Tradução"
        )

    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    traslated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=traslated,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()

    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    traslated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=traslated,
    )
