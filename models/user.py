class User:
    def __init__(self, user_id, first_name, last_name, personal_email, phone, password_hash, profile_picture, created_date, modified_date):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.personal_email = personal_email
        self.phone = phone
        self.password_hash = password_hash
        self.profile_picture = profile_picture
        self.created_date = created_date
        self.modified_date = modified_date