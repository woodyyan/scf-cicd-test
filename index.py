import requests


def main_handler(event, context):
    print("start main handler")

    response = requests.get("https://www.baidu.com/")
    print(response.content)


if __name__ == '__main__':
    main_handler(None, None)
