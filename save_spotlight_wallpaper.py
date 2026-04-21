import os
import shutil
import ctypes

SPI_GETDESKWALLPAPER = 0x0073
MAX_PATH = 260


def get_current_desktop_wallpaper():
    buffer = ctypes.create_unicode_buffer(MAX_PATH)
    if ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, buffer, 0):
        path = buffer.value
        return path if path and os.path.isfile(path) else None
    return None


def is_image_file(path):
    try:
        with open(path, 'rb') as f:
            header = f.read(8)
        return header.startswith(b'\xff\xd8\xff') or header.startswith(b'\x89PNG\r\n\x1a\n')
    except OSError:
        return False


def find_latest_spotlight_image():
    user_profile = os.path.expanduser('~')
    assets_path = os.path.join(
        user_profile,
        'AppData', 'Local', 'Packages',
        'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy',
        'LocalState', 'Assets'
    )

    if not os.path.isdir(assets_path):
        return None

    candidates = []
    for entry in os.listdir(assets_path):
        full_path = os.path.join(assets_path, entry)
        if not os.path.isfile(full_path):
            continue
        if os.path.getsize(full_path) < 50_000:
            continue
        if is_image_file(full_path):
            candidates.append(full_path)

    if not candidates:
        return None

    return max(candidates, key=os.path.getmtime)


def main():
    desktop_wallpaper = get_current_desktop_wallpaper()
    if desktop_wallpaper and is_image_file(desktop_wallpaper):
        source = desktop_wallpaper
        file_name = 'current_wallpaper' + os.path.splitext(desktop_wallpaper)[1]
        print('Detected active desktop wallpaper.')
    else:
        source = find_latest_spotlight_image()
        file_name = 'current_spotlight.jpg'
        if source:
            print('Detected Windows Spotlight image from assets folder.')

    if not source:
        print('Could not locate the current wallpaper or Spotlight image.')
        return

    dest = os.path.join(os.path.expanduser('~'), 'Desktop', file_name)
    shutil.copy(source, dest)
    print(f'Saved current wallpaper to: {dest}')


if __name__ == '__main__':
    main()
