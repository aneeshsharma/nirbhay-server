import mysql.connector
import string
import random


def verify(user_data):
    fields = ['username', 'name', 'password', 'aadhar', 'mobile', 'alt_mobile']
    for x in fields:
        if x not in user_data:
            print(x + "N/A")
            return False
    return True


def register(user_data):
    db = mysql.connector.connect(
        host="localhost",
        user="joe",
        passwd="joemama",
        database="hackverse",
        auth_plugin="mysql_native_password"
    )

    cursor = db.cursor()

    query = "SELECT username FROM users WHERE username='" + \
        user_data['username'] + "';"

    cursor.execute(query)

    res = cursor.fetchall()

    if len(res) >= 1:
        return "USERNAME ALREADY EXISTS"

    key = ''.join([random.choice(string.ascii_uppercase + string.digits)
                   for _ in range(20)])

    query = "INSERT INTO users (username, name, password, aadhar, mobile, alt_mobile, secret_key) VALUES ('" +\
        user_data['username'] + "', '" +\
        user_data['name'] + "', '" +\
        user_data['password'] + "', '" +\
        user_data['aadhar'] + "', '" +\
        user_data['mobile'] + "', '" +\
        user_data['alt_mobile'] + "', '" +\
        key + "');"

    print("Querying: ", query)

    cursor.execute(query)
    db.commit()

    print(cursor.rowcount, "records inserted")

    return "SUCCESS:"+key


def get_key(username, password):
    db = mysql.connector.connect(
        host="localhost",
        user="joe",
        passwd="joemama",
        database="hackverse",
        auth_plugin="mysql_native_password"
    )

    cursor = db.cursor()

    query = "SELECT password, secret_key FROM users WHERE username='" + username + "';"

    cursor.execute(query)

    res = cursor.fetchall()

    if len(res) > 1:
        return "SERVER ERROR"

    if len(res) < 1:
        return "INVALID USERNAME"

    if res[0][0] != password:
        return "INVALID PASSWORD"

    return res[0][1]


def update_location(lat, lng, secret_key):
    db = mysql.connector.connect(
        host="localhost",
        user="joe",
        passwd="joemama",
        database="hackverse",
        auth_plugin="mysql_native_password"
    )

    cursor = db.cursor()

    query = "UPDATE users SET lat=" + \
        lat + ", lng=" + lng + \
        " WHERE secret_key='" + secret_key + "';"

    cursor.execute(query)
    db.commit()

    if cursor.rowcount < 1:
        return "UNABLE TO UPDATE"

    return "SUCCESS"


def update_dest(lat, lng, secret_key):
    db = mysql.connector.connect(
        host="localhost",
        user="joe",
        passwd="joemama",
        database="hackverse",
        auth_plugin="mysql_native_password"
    )

    cursor = db.cursor()

    query = "UPDATE users SET destLat=" + \
        lat + ", destLng=" + lng + \
        " WHERE secret_key='" + secret_key + "';"

    cursor.execute(query)
    db.commit()

    if cursor.rowcount < 1:
        return "UNABLE TO UPDATE"

    return "SUCCESS"
