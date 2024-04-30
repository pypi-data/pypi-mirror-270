# @singleton

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


# @private

def private(cls):
    def wrapper(*args, **kwargs):
        raise Exception("This class is private and cannot be accessed from outside the module!")
    return wrapper

# Import configuration from config/config.py and config/configContainer.py to allow it to be used in other modules when package is imported.

def config(configContainer):
    from config import config
    return config(configContainer)

def configContainer(name, path, extension):
    from config import configContainer
    return configContainer(name, path, extension)



