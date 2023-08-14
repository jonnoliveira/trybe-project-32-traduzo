from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    users = [
        {"name": "Jonn", "level": "admin", "token": "1234"},
    ]
    historys = [
        {
            "text-to-translate": "Do you love music?",
            "translate-from": "en",
            "translate-to": "pt",
        },
        {
            "text-to-translate": "Do you love Elvis?",
            "translate-from": "en",
            "translate-to": "pt",
        },
    ]

    for user in users:
        UserModel(user).save()

    for history in historys:
        HistoryModel(history).save()

    user = UserModel.find_one({"name": "Jonn"})
    history = HistoryModel.find_one(
        {"text-to-translate": "Do you love Elvis?"}
    )

    app_test.delete(
        f"/admin/history/{history.data['_id']}",
        headers={
            "Authorization": user.data["token"],
            "User": user.data["name"],
        },
    )
