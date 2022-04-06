import snowflake.client


def get_snowflake_uuid():
    guid = snowflake.client.get_guid()
    return guid


res = get_snowflake_uuid()
print(res)
