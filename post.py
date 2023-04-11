class Post:
    def __init__(self, number, user_uid, content, upload_date, update_date, like_count, reply_count, post_type, is_deleted, is_anonymous):
        self.number = number
        self.user_uid = user_uid
        self.content = content
        self.upload_date = upload_date
        self.update_date = update_date
        self.like_count = like_count
        self.reply_count = reply_count
        self.post_type = post_type
        self.is_deleted = is_deleted
        self.is_anonymous = is_anonymous

