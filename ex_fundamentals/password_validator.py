def password_validator(password):
    password_lenght = True
    valid_chars = True
    num_counter = 0
    if 6 <= len(password) <= 10:
        pass
    else:
        password_lenght = False
    for cheractor in password:
        if 65 <= ord(cheractor) <= 90 or 97 <= ord(cheractor) <= 122 or 48 <= ord(cheractor) <= 57:
            if 48 <= ord(cheractor) <= 57:
                num_counter += 1
        else:
            valid_chars = False

    if not password_lenght:
        print('Password must be between 6 and 10 characters')
    if not valid_chars:
        print('Password must consist only of letters and digits')
    if num_counter < 2:
        print('Password must have at least 2 digits')
    if password_lenght and valid_chars and num_counter >= 2:
        print('Password is valid')


password = input()
password_validator(password)
