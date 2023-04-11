import pymysql

import post

from enum import Enum


class Flags(Enum):
    NO = 0
    OK = 1
    TABLE_POST = "posts"


flags = Flags


def select_post():
    db = pymysql.connect(host="localhost", user="root", password="gozldgkwlak0!z", charset="utf8")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('use emotion_db;')

    cursor.execute(f'select * from {flags.TABLE_POST.value} order by number desc;')
    value = cursor.fetchall()

    db.commit()
    db.close()

    return value


def insert_post(_post: post.Post):
    db = pymysql.connect(host="localhost", user="root", password="gozldgkwlak0!z", charset="utf8")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('use emotion_db;')

    execute_str = f'INSERT INTO `emotion_db`.`{flags.TABLE_POST.value}` (' \
                  '`user_uid`, ' \
                  '`content`, ' \
                  '`upload_date`, ' \
                  '`update_date`, ' \
                  '`like_count`, ' \
                  '`reply_count`, ' \
                  '`post_type`, ' \
                  '`is_deleted`, ' \
                  '`is_anonymous`) ' \
                  f'values (' \
                  f'"{_post.user_uid}", ' \
                  f'"{_post.content}", ' \
                  f'"{_post.upload_date}", ' \
                  f'"{_post.update_date}", ' \
                  f'"{_post.like_count}", ' \
                  f'"{_post.reply_count}", ' \
                  f'"{_post.post_type}", ' \
                  f'"{_post.is_deleted}",' \
                  f'"{_post.is_anonymous}"' \
                  ');'

    cursor.execute(execute_str)
    db.commit()
    db.close()


def update_post(_post: post.Post):
    db = pymysql.connect(host="localhost", user="root", password="gozldgkwlak0!z", charset="utf8")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('use emotion_db;')

    execute_str = f'UPDATE `emotion_db`.`{flags.TABLE_POST.value}` SET ' \
                  f'`content` = "{_post.content}",' \
                  f'`update_date` = "{_post.update_date}",' \
                  f'`post_type` = "{_post.post_type}",' \
                  f'`is_anonymous` = "{_post.is_anonymous}"' \
                  f'WHERE `number` = "{_post.number}";'

    cursor.execute(execute_str)
    db.commit()
    db.close()


def delete_flag_change_post(_post: post.Post):
    db = pymysql.connect(host="localhost", user="root", password="gozldgkwlak0!z", charset="utf8")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('use emotion_db;')

    execute_str = f'UPDATE `emotion_db`.`{flags.TABLE_POST.value}` SET ' \
                  f'`update_date` = "{_post.update_date}",' \
                  f'`is_deleted` = "{_post.is_deleted}"' \
                  f'WHERE `number` = "{_post.number}";'

    cursor.execute(execute_str)
    db.commit()
    db.close()


def delete_post(_post: post.Post):
    db = pymysql.connect(host="localhost", user="root", password="gozldgkwlak0!z", charset="utf8")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('use emotion_db;')

    execute_str = f'DELETE FROM `emotion_db`.`{flags.TABLE_POST.value}` WHERE `number` = "{_post.number};'

    cursor.execute(execute_str)
    db.commit()
    db.close()
