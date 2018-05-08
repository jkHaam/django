import re
def validate_phone_number(number):
    #핸드폰 체크
    if not re.match(r'^01[016789][0-9]\d{6,7}$', number):
        return False
    return True

print(validate_phone_number('01012341234'))
print(validate_phone_number('0101112222'))
print(validate_phone_number('010111112222'))










