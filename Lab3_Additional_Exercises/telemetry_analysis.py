def log_process(func):

    def wrapper(*args, **kwargs):

        print(f"[LOG] {func.__name__}")

        return func(*args, **kwargs)

    return wrapper