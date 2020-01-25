import mysql.connector


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

    query = "INSERT INTO users (username, name, password, aadhar, mobile, alt_mobile) VALUES ('" +\
        user_data['username'] + "', '" +\
        user_data['name'] + "', '" +\
        user_data['password'] + "', '" +\
        user_data['aadhar'] + "', '" +\
        user_data['mobile'] + "', '" +\
        user_data['alt_mobile'] + "');"

    cursor.execute(query)
    db.commit()

    print(cursor.rowcount, "records inserted")

    return "SUCCESS"
