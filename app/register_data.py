def verify(user_data):
    fields = ['username', 'name', 'password', 'aadhar', 'mobile', 'alt_mobile']
    for x in fields:
        if x not in user_data:
            print(x + "N/A")
            return False
    return True
