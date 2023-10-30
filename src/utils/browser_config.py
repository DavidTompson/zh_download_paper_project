
from selenium.webdriver.chrome.options import Options
class BrowserConfig:
    def __init__(self) -> None:
        self.options = Options
        self.options.add_argument("--incognito")
        self.options.add_argument("--disable-domain-reliability")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-client-side-phishing-detection")
        self.options.add_argument("--no-first-run")
        self.options.add_argument("--use-fake-device-for-media-stream")
        self.options.add_argument("--autoplay-policy=user-gesture-required")
        self.options.add_argument("--disable-features=ScriptStreaming")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-save-password-bubble")
        self.options.add_argument("--mute-audio")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-software-rasterizer")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-webgl")
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument("--no-default-browser-check")
        self.options.add_argument("--disable-full-form-autofill-ios")
        self.options.add_argument("--disable-autofill-keyboard-accessory-view[8]")
        self.options.add_argument("--disable-single-click-autofill")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-blink-features")
        # 禁用实验性QUIC协议
        self.options.add_experimental_option("excludeSwitches", ["enable-quic"])
        
