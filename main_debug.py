import ok
from src.config import config
from src.ui.SponsorDialog import install_sponsor_dialog
from src.ui.GuideTab import install_guide_handler

if __name__ == '__main__':
    install_sponsor_dialog()
    install_guide_handler()
    config = config
    config['debug'] = True
    ok = ok.OK(config)
    ok.start()
