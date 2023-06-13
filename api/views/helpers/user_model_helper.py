import datetime


def generate_id(data: str) -> str:
    _id = ""
    current_time = datetime.datetime.now()
    if data != "":
        _id = data[:2] + str(current_time.year)[2:] + str(current_time.month) \
              + str(current_time.day) + str(current_time.hour) + str(current_time.minute) + \
              str(current_time.second) + str(current_time.microsecond)[:2]
    if _id != "":
        return _id
    else:
        raise ValueError("ID cannot be created. Please try again.")
