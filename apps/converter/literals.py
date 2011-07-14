from converter.conf.settings import DEFAULT_OPTIONS
from converter.conf.settings import LOW_QUALITY_OPTIONS
from converter.conf.settings import HIGH_QUALITY_OPTIONS
from converter.conf.settings import PRINT_QUALITY_OPTIONS

DEFAULT_ZOOM_LEVEL = 100
DEFAULT_ROTATION = 0
DEFAULT_PAGE_INDEX_NUMBER = 0
DEFAULT_FILE_FORMAT = u'jpg'
DEFAULT_OCR_FILE_FORMAT = u'tif'

QUALITY_DEFAULT = u'quality_default'
QUALITY_LOW = u'quality_low'
QUALITY_HIGH = u'quality_high'
QUALITY_PRINT = u'quality_print'

QUALITY_SETTINGS = {
    QUALITY_DEFAULT: DEFAULT_OPTIONS,
    QUALITY_LOW: LOW_QUALITY_OPTIONS,
    QUALITY_HIGH: HIGH_QUALITY_OPTIONS,
    QUALITY_PRINT: PRINT_QUALITY_OPTIONS
}
