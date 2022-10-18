import botometer


def initialize_boto():
    rapidapi_key = "rapidapi_key"
    twitter_app_auth = {
        'consumer_key': 'consumer_key',
        'consumer_secret': 'consumer_secret',
        'access_token': 'access_token',
        'access_token_secret': 'access_token_secret',
    }
    return botometer.Botometer(wait_on_ratelimit=True,
                               rapidapi_key=rapidapi_key,
                               **twitter_app_auth)


if __name__ == '__main__':
    bom = initialize_boto()
    # bom.check_accounts_in(['@clayadavis', '@onurvarol', '@jabawack'])
    print(bom.check_account('@clayadavis'))