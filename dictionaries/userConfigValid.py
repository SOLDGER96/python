test_settings = {
        'theme': 'dark',
        'notifications': 'enabled',
        'volume': 'high'
    }



def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return (f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = str(value).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    op = 'Current User Settings:\n'
    for key, value in settings.items():
        op += f"{key.capitalize()}: {value}\n"
    return op

print(view_settings(test_settings))