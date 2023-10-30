from dataclasses import dataclass
from environs import Env

import os
import dotenv

@dataclass
class TgBot:
    token: str      #Токен для доступа к телеграм_боту
    admin_ids: list[int]    #список id админов бота

@dataclass
class Config:
    tg_bot: TgBot

def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env.str('BOT_TOKEN3'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))))   

# env: Env = Env()
# env.read_env('tasks_bot/.env')

# tg_bot=TgBot(token=env('BOT_TOKEN3'),
#              admin_ids=list(map(int, env.list('ADMIN_IDS'))))
# print(Config(tg_bot))

print(load_config('tasks_bot/.env'))

