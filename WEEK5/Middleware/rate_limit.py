request_count={}


def allow_request(user):

    count=request_count.get(user,0)

    if count>=5:

        return False

    request_count[user]=count+1

    return True