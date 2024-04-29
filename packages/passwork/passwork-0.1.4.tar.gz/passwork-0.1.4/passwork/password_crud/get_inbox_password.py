import json
from loguru import logger
from passwork.passwork_api import PassworkAPI


def get_inbox_password(api: PassworkAPI, inbox_password_id: str, log_pretty_data: bool = True) -> dict:

    """
    Retrieve inbox password information from Passwork API.

    Args:
        api (PassworkAPI): An instance of PassworkAPI class initialized with appropriate credentials.
        inbox_password_id (str): The unique identifier of the password to retrieve.
        log_pretty_data (bool): Whether to log the retrieved password information. Defaults to True.

    Returns:
        dict: A dictionary containing the retrieved inbox password information.

    This function authenticates with the Passwork API, retrieves inbox password details, including associated vault,
    custom fields, attachments, and plaintext value. If specified, it
    logs this information using the logger.

    Example usage:
        api = PassworkAPI(credentials)\n
        password_info = get_inbox_password(api, 'password123')

    Raises:
        ValueError: If inbox_password_id is empty or None.
    """

    api.login()
    api.get_user_info()

    inbox_item = api.get_inbox_password(inbox_password_id)
    inbox_password_item = inbox_item["password"]
    encryption_key = api.get_inbox_encryption_key(inbox_item)

    # get inbox password customs
    inbox_password_item["custom"] = api.get_customs(
        password_item=inbox_password_item, password_encryption_key=encryption_key
    )

    # download inbox password attachments
    api.get_attachments(
        password_item=inbox_password_item, password_encryption_key=encryption_key
    )

    # get inbox password plain text
    password_plain_text = api.get_password_plain_text(
        password_item=inbox_password_item, password_encryption_key=encryption_key
    )

    # receive full inbox password info
    inbox_password_info = {
        "inbox_item": inbox_item,
        "passwordPlainText": password_plain_text,
    }

    pretty_data = json.dumps(inbox_password_info, indent=4)
    if log_pretty_data:
        logger.success(pretty_data)

    return inbox_password_info

