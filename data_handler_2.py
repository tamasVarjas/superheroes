import bcrypt
import database_common


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@database_common.connection_handler
def save_registration(cursor, username, password, image):
    cursor.execute("""
                    INSERT INTO users (username, password, image) 
                    VALUES (%(username)s, %(password)s, %(image)s);
                    """,
                   {'username': username, 'password': password, 'image': image})

@database_common.connection_handler
def save_registration_without_image(cursor, username, password):
    cursor.execute("""
                    INSERT INTO users (username, password) 
                    VALUES (%(username)s, %(password)s);
                    """,
                   {'username': username, 'password': password})



