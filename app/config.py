import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGES_DIR = '{}/images'.format(BASE_DIR)

APP_NAME = 'SkyPhone'

APP_VERSION = '1.0.0'

APP_LOGO = '{}/logo.png'.format(IMAGES_DIR)

APP_ICON = '{}/icon.png'.format(IMAGES_DIR)

APP_ICON_MICROPHONE_ON = '{}/microphone-alt-solid.png'.format(IMAGES_DIR)

APP_ICON_MICROPHONE_OFF = '{}/microphone-alt-slash-solid.png'.format(IMAGES_DIR)

APP_ICON_VOLUME_ON = '{}/volume-up-solid.png'.format(IMAGES_DIR)

APP_ICON_VOLUME_OFF = '{}/volume-mute-solid.png'.format(IMAGES_DIR)

APP_DEFAULT_BACKGROUND_COLOR = '#030304'