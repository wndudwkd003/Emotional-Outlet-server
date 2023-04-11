class Post:
    number = None
    user_uid = None
    content = None
    upload_date = None
    update_date = None
    like_count = None
    reply_count = None
    post_type = None
    is_deleted = None
    is_anonymous = None

    def __init__(self, number, user_uid, content, upload_date, update_date, like_count, reply_count, post_type,
                 is_deleted, is_anonymous):
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
