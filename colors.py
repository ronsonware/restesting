class Color(object):
    HEADER = '\033[95m'
    SUCCESS_BLUE = '\033[94m'
    SUCCESS_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def onePrintColorfull(colors, string):
        print(colors+string+Color.NORMAL)
