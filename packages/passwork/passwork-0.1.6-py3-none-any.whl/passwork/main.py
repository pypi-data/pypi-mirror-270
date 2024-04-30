from passwork.password_crud import get_inbox_password
from passwork.passwork_api import PassworkAPI

api = PassworkAPI(
    host="https://v6-python-test-no-crypt.passwork.nl/api/v4",
    api_key="zZwiX2NpZFYGcGj51lsXGeAiSZ9eHVkUUGZtlq2OQbBmvvSS3C7jSl5d71Fu"
)
get_inbox_password(api, inbox_password_id="6629b831b76db5b6b10ce236")
