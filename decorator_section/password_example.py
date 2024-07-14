from functools import wraps

user = dict(username="jose", access_level="guest")


def make_secure(access_level):
    def decorator(fn):
        @wraps(fn)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return fn(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return secure_function

    return decorator


@make_secure("admin")
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "5678"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


print(get_password("admin"))
print(get_dashboard_password())
