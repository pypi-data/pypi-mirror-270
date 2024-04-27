import logging

from api_nichotined import Api


class TestApi(Api):
    def __init__(self):
        super().__init__("https://restcountries.com")

    def get_upload(self):
        return self.get(path="/v3.1/name/indonesia")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    response = TestApi().get_upload()
    print(response.status_code)
    print(response.request)
