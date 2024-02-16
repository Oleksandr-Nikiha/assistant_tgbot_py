from models.user import User


async def parse_users(data):
    user_list = [User(**user_dict) for user_dict in data]

    return user_list