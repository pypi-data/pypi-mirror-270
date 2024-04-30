import os
from paloalto_panorama_sdk.key_manager import KeyManager
from paloalto_panorama_sdk.service_manager import ServiceManager
from dotenv import load_dotenv

load_dotenv()


class PanoramaSDK:
    def __init__(self, url, username, password, verify=True):
        self.url = url
        self.username = username
        self.password = password
        self.apikey = KeyManager.get_api_key(
            panorama_url=self.url,
            user=self.username,
            password=self.password,
            verify=verify
        )
        self.service = ServiceManager(panorama_url=self.url, api_key=self.apikey, verify=verify)


if __name__ == '__main__':
    panSDK = PanoramaSDK(
        url=os.getenv("url", ""),
        username=os.getenv("user", "test"),
        password=os.getenv("password", "testpass")
    )
    print(panSDK.apikey)
