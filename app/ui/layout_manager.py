from app.core.language_manager import language_manager


def is_rtl():

    return (
        language_manager.get_interface_language()
        == "ar"
    )


def get_side():

    if is_rtl():
        return "right"

    return "left"


def get_anchor():

    if is_rtl():
        return "e"

    return "w"