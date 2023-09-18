import nonebot
from nonebot.adapters.onebot.v12 import Adapter as OneBot_v12_Adapter

# initialization
nonebot.init(_env_file=".env.dev")

# register adapter
driver = nonebot.get_driver()
driver.register_adapter(OneBot_v12_Adapter)

# initialize global/static variable
print(driver.config)

# load plugins
nonebot.load_from_toml("pyproject.toml")

# if __name__ == "__main__":
#     nonebot.run()