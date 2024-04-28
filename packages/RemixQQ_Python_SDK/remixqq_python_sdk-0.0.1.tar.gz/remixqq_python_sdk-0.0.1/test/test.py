from remixqq_python_sdk.app import App

bot = App("http://114.55.116.67:8081/MyQQHTTPAPI", "404", "1328382485")

print(bot.get_cookies())