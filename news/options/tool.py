from datetime import datetime
GENDER = (
    (True, "Kişi"),
    (False, "Qadın")
)


def get_avatar_path(intance, filename):
    return "profile/%s_%s" % (datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), filename)