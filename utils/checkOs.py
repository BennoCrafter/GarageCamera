import platform

# thanks chatgpt!
def is_raspberry_pi():
    pi_platforms = ['armv7l', 'armv6l']
    return platform.machine() in pi_platforms

