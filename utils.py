import os


def get_assets_folder_path():
    return os.path.join(os.path.dirname(os.getcwd()), 'assets')


if __name__ == '__main__':
    a = get_assets_folder_path()
    print("kehjre")