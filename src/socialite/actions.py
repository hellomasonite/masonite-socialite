def do_complete(backend, user=None, redirect_name='next', *args, **kwargs):
    data = backend.strategy.request_data()

    user = backend.complete(user=user, *args, **kwargs)

    redirect_value = backend.strategy.session_get(redirect_name, '') or \
                     data.get(redirect_name, '')
    return user
