from BotAmino import BotAmino, Parameters
# from pymino import Bot
from MessageType import *
from aminofix.lib.util.exceptions import *
import time
import re
import logging


def main():
    client = BotAmino("fswap@bk.ru", "aboba123")
    client.self_callable = True
    client.activity = True

    # bot = Bot()
    # bot.run(sid=client.sid)
    bot_chat_id = "30ac29f7-ce70-0d03-1b62-e0432901ab42"
    my_chat_id = "6396e92b-4c3f-0582-327b-3db6ddbb3433"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    fmt = logging.Formatter(fmt="[%(levelname)s] %(asctime)s — %(message)s")
    handler.setFormatter(fmt)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    file_handler = logging.FileHandler(filename="utilities\\log.txt", encoding="utf-16")
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    def in_staff(data):
        return data.subClient.is_in_staff(data.authorId)

    def get_id_from_code(code: str) -> str:
        return client.get_from_code(code).objectId

    def catch_spammer(data, uid: str = "", chat_id: str = "", nickname: str = ""):
        logger.info(f"Catched spammer: {nickname}")
        user_list = data.subClient.get_chat_users(chatId=chat_id, size=100).userId
        for user_id in user_list:
            if user_id == client.userId:
                continue
            data.subClient.send_message(chatId=bot_chat_id, message=f'!id_kick {chat_id} {user_id}')
            time.sleep(31)
        try:
            data.subClient.leave_chat(chatId=chat_id)
        except RequestedNoLongerExists:
            pass
        data.subClient.send_message(chatId=bot_chat_id, message=f'!id_hide {chat_id}')
        time.sleep(4)
        data.subClient.send_message(chatId=bot_chat_id, message=f'''!id_ban {uid} {nickname}''')
        time.sleep(4)
        data.subClient.send_message(chatId=bot_chat_id, message=f"!atb {nickname}")

    @client.command("chatId")
    def get_chat_id(data):
        data.subClient.send_message(chatId=data.chatId, message=data.chatId)

    @client.command("userId")
    def get_user_id(data):
        data.subClient.send_message(chatId=data.chatId, message=data.authorId)

    @client.command(["watch_ad", "wa"])
    def watch_ad(data: Parameters):
        data.subClient.watch_ad()

    @client.command(["farm_coins", "fc"])
    def farm_coins(data: Parameters):
        n = 50000
        blog_id = get_id_from_code("95dk3tt")
        while n > 0:
            coins = min(data.subClient.get_wallet_amount(), 500)
            data.subClient.watch_ad()
            time.sleep(5)
            if coins > 1:
                data.subClient.pay(coins=coins, blogId=blog_id)
                logger.info(f"Отправлено {coins} монет")
                time.sleep(31)

    @client.command("message")
    def message(data):
        data.subClient.send_message(chatId=data.chatId, message="success")

    @client.command(["invite_to_chat", "itc"])
    def invite_to_chat(data, user_link: str, chat_link: str = ""):
        user_id = client.get_from_code(user_link).objectId
        chat_id = client.get_from_code(chat_link).objectId if chat_link else data.chatId
        data.subClient.invite_to_chat(userId=user_id, chatId=chat_id)

    @client.command("leave_chats", condition=in_staff)
    def leave_chats(data):
        chats = data.subClient.get_chat_threads(start=0, size=100).chatId
        must_chats = [bot_chat_id, my_chat_id]
        for chat in chats:
            if chat not in must_chats:
                data.subClient.leave_chat(chatId=chat)

    def _check_messages(data):
        chats = data.subClient.get_chat_threads(start=0, size=10).chatId
        for chat in chats:
            if chat == bot_chat_id:
                continue
            message_list = data.subClient.get_chat_messages(chatId=chat, size=3)
            for uid, content, nick in zip(message_list.author.userId, message_list.content, message_list.author.nickname):
                if content is None:
                    continue
                content = str(content)
                if ("t.me/" in content) or ("aminoapps.com/" in content):
                    catch_spammer(data, uid=uid, chat_id=chat, nickname=nick)

    @client.command(["cm"])
    def check_messages(data):
        _check_messages(data)

    @client.command(["checking", "cing"], condition=in_staff)
    def checkin(data):
        n = 50000
        data.subClient.send_message(chatId=data.chatId, message="Обход пошел", replyTo=data.messageId)
        while n > 0:
            try:
                _check_messages(data)
            except Exception as e:
                logger.info(repr(e))
            time.sleep(30)
            data.subClient.send_message(chatId=bot_chat_id, message="!cu")
            time.sleep(30)
            n -= 1

    def detect_link(m: str) -> str:
        regex_am = r"(aminoapps.[^\s]+)"
        regex_tm = r"(t.me[^\s]+)"
        links_am = re.findall(regex_am, m)
        links_tm = re.findall(regex_tm, m)
        result = links_am if links_am else links_tm
        return result[0] if result else ""

    @client.on_all()
    def on_message(data):
        content = str(data.message)
        #print(content)
        link = detect_link(content)
        mtype = data.info.message.type
        default_type = [0, 3, 100, 103, 119]
        if mtype not in default_type:
            print(mtype)
            print(content)
        raid_types = {TYPE_USER_SHARE_EXURL, TYPE_USER_SHARE_USER, VIDEO_CHAT_NOT_DECLINED,
                      AVATAR_CHAT_NOT_ANSWERED, AVATAR_CHAT_NOT_CANCELLED, AVATAR_CHAT_NOT_DECLINED,
                      DELETE_MESSAGE}
        if mtype in raid_types:
            if link and "aminoapps.com/p/" not in link:
                print('catched spamer')
                catch_spammer(data, uid=data.authorId, chat_id=data.chatId, nickname=data.author)

    @client.on_message()
    def text_message(data):
        content = str(data.message)
        link = detect_link(content)
        if link and "aminoapps.com/p/" not in link:
            #print('catched spam message')
            catch_spammer(data, uid=data.authorId, chat_id=data.chatId, nickname=data.author)

    client.launch(True)
    logger.info(f"{client.profile.nickname} ready")


if __name__ == '__main__':
    try:
        main()
    except IpTemporaryBan:
        with open('C:\\Users\\Denis\\Desktop\\test\\loga.txt', 'w', encoding='utf-8') as f:
            f.write('ip ban')
