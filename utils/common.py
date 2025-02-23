import datetime

def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def set_default_values(user_data):
    user_data['created_dt'] = get_current_timestamp()
    user_data['modified_dt'] = get_current_timestamp()
    return user_data