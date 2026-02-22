from flask import session, abort



def admin_only_view(funk):
    def decorator(*args, **kwargs):
        if session.get("user_id") is None:
            abort(401)
        if session.get('role') != 1:
            abort(403)
        return funk(*args, **kwargs)
    return decorator