from BotAmino import BotAmino, Parameters
from aminofix.lib.util.exceptions import *
from aminofix.lib.util.helpers import update_deviceId
from MessageType import *
from PIL import Image, UnidentifiedImageError
# from ytdl.ytdownloader import download_mp3
import httplib2
import re
import time
import logging
import os


def restart():
    with open('C:\\Users\\Denis\\Desktop\\test\\logt.txt', 'w', encoding='utf-8') as ft,\
         open('C:\\Users\\Denis\\Desktop\\test\\loga.txt', 'w', encoding='utf-8') as fa:
        ft.write('ip ban')
        fa.write('ip ban')


def main():
    # TODO: get_user_blogs(self, userId: str, start: int = 0, size: int = 25)
    # TODO: get_blog_info(self, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None)
    # TODO: get_blog_comments(self, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None, sorting: str = "newest", start: int = 0, size: int = 25)
    # TODO: get_blog_categories(self, size: int = 25)
    # TODO: get_blogs_by_category(self, categoryId: str,start: int = 0, size: int = 25)
    # TODO: get_recent_blogs(self, pageToken: str = None, start: int = 0, size: int = 25)
    # TODO: get_hidden_blogs(self, start: int = 0, size: int = 25)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    fmt = logging.Formatter(fmt="[%(levelname)s] %(asctime)s — %(message)s")
    handler.setFormatter(fmt)
    handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(filename="utilities\\log.txt", encoding="utf-16")
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(file_handler)

    # http_proxy  = "http://125.141.133.46:5566"
    # https_proxy = "https://125.141.133.46:5566"
    # ftp_proxy   = "ftp://125.141.133.46:5566"
    #
    # proxies = {
    #               "http": http_proxy,
    #               "https": https_proxy,
    #               "ftp": ftp_proxy
    #             }

    client = BotAmino("buchnev_dm14@mail.ru", "swag1437")
    client.self_callable = True
    client.no_command_message = "Нет такой команды"
    client.lock_message = "Эта команда заблокирована"
    client.spam_message = "Харош спамить"

    my_chat_id = "8c41b3d7-824f-0881-2919-ddf5f4ba9f71"
    admin_chat_id = "28d2d741-0726-4d78-be58-fa9ed56125b4"
    flud_chat_id = "caaf39f2-1f88-4492-95a2-2b529a3425ef"
    general_chat_id = "9d160a1e-ad90-4abe-9034-1cea15bd5753"
    search_chat_id = "d7547e21-54a5-43fb-a4ef-500c6727cc67"
    rp_chat_id = "9f44a213-05b8-40be-a039-05e1b1bec5fe"
    last_drop_chat_id = "b8969095-4766-43b5-9667-3651ef9a1849"
    cinema_chat_id = "399b5956-3f79-4133-9558-26e8d3a6a39e"

    bot_id = "90cc9e93-5560-457f-be4c-9cc1d73cb9ac"
    ruch_id = "d15eee7d-5d5f-439f-bb60-4774cf48ee82"
    fswap_id = "7f1bc46f-9b10-487c-a52e-7c82fe3d12ee"

    bots_id = {bot_id, ruch_id, fswap_id}
    reporters_id = {ruch_id, fswap_id}
    holy_chats = {my_chat_id, admin_chat_id, flud_chat_id, general_chat_id,
                  search_chat_id, rp_chat_id, last_drop_chat_id, cinema_chat_id}
    general_chats = {flud_chat_id, general_chat_id, search_chat_id, rp_chat_id, last_drop_chat_id, cinema_chat_id}

    kick_stick_ids = {"1035df13-b523-4d57-8850-420d7948bffc", "4e476d65-3119-4cdc-9beb-25d91aa6dcb8"}
    delete_stick_ids = {"203466a8-3eb1-488a-94ae-d61f397e6461", "abd356ed-f6d5-4e8d-ad47-c052ff8291e0"}
    troll_dict = {}
    loh_set = {"aace8472-d513-46c9-bd58-bad8700a9af0"}
    troll_flag = False

    banfile = 'utilities\\banlist.txt'
    banlist = set()
    try:
        with open(banfile, "r", encoding='utf-16') as file:
            for banlistmember in file.readlines():
                banlist.add(banlistmember.strip())
    except FileNotFoundError:
        a = open(banfile, "w")
        a.close()

    banned_words = set()
    with open("utilities\\banned_words.txt", "r", encoding="utf-16") as file:
        for line in file:
            banned_words.add(line.strip())

    hex_colors = dict()
    with open("utilities\\hex_colors.txt", "r", encoding="utf-8") as file:
        for line in file:
            key, val = line.strip().split()
            hex_colors[key] = val

    def in_staff(data: Parameters) -> bool:
        return data.subClient.is_in_staff(data.authorId)

    def is_agent(data: Parameters) -> bool:
        return data.subClient.is_agent(data.authorId)

    def is_reporter(data: Parameters) -> bool:
        return data.authorId in reporters_id

    def reporter_or_staff(data: Parameters) -> bool:
        return in_staff(data) or is_reporter(data)

    def get_id_from_code(code: str) -> str:
        return client.get_from_code(code).objectId

    reporters_id.add(get_id_from_code("9djnpt"))
    reporters_id.add(get_id_from_code("e9kwk3"))

    def get_current_time() -> str:
        t = time.localtime()
        return f"{((t.tm_hour - 2) % 24):0>2}:{t.tm_min:0>2}:{t.tm_sec:0>2}"

    def reply(data: Parameters, message: str):
        data.subClient.send_message(chatId=data.chatId, message=message, replyTo=data.messageId)

    @client.command(["reply_info", "ri"], condition=is_agent)
    def reply_info(data: Parameters):
        print(f"{data.replySrc = }")
        print(f"{data.replyId = }")
        print(f"{data.replyMsg = }")
        print(f"{data.replyUserId = }")

    def catch_spammer(data: Parameters, user_id="", chat_id="", message_id="", reason=""):
        current_time = get_current_time()
        data.subClient.delete_message(chatId=chat_id, messageId=message_id, asStaff=True, reason=f"{current_time} {reason}")
        data.subClient.kick(chatId=chat_id, userId=user_id, allowRejoin=True)
        data.subClient.ban(userId=user_id, reason=f"{current_time} {reason}")

    @client.command(["count_users"], condition=is_agent)
    def count_users(data: Parameters):
        com_id = data.comId
        count = client.get_community_info(comId=com_id).usersCount
        reply(data, message=f"Количество пользователей в сообществе: {count}")

    @client.command(["restart", "перезапуск"], condition=in_staff)
    def restart_bot(data: Parameters):
        reply(data, "Начинаю перезапуск")
        restart()

    @client.command(["set_prefix", "sp", "назначить_префикс", "нп"], condition=is_agent)
    def set_prefix(data: Parameters, prefix: str):
        help_admin = []
        with open("utilities\\help_admin.txt", "r", encoding="utf-8") as file:
            for line in file:
                help_admin.append(line.replace(client.prefix, prefix))

        with open("utilities\\help_admin.txt", "w", encoding="utf-8") as file:
            for line in help_admin:
                file.write(line)
        reply(data, f"Префикс для команд изменен с {client.prefix} на {prefix}")
        client.prefix = prefix
        data.subClient.set_prefix(prefix)

    @client.answer(["get_prefix", "gp", "узнать_префикс", "префикс", "prefix"])
    def get_prefix(data: Parameters):
        reply(data, f"Префикс для использования команд: {client.prefix}")

    @client.command(["lock_command", "заблочить_команду"], condition=is_agent)
    def add_locked_command(data: Parameters):
        content = data.message.split()
        data.subClient.add_locked_command(content)
        reply(data, f"")

    @client.command(["unlock_command", "разблочить_команду"], condition=is_agent)
    def remove_locked_command(data: Parameters):
        content = data.message.split()
        data.subClient.remove_locked_command(content)

    @client.command(["add_banword", "abw", "добавить_банворд", "дбв"], condition=in_staff)
    def add_ban_word(data: Parameters):
        ban_words = data.message.split()
        with open("utilities\\banned_words.txt", "a", encoding="utf-16") as file:
            for ban_word in ban_words:
                if ban_word.lower() in banned_words:
                    ban_words.remove(ban_word)
                else:
                    banned_words.add(ban_word.lower())
                    file.write(ban_word.lower() + "\n")
        if ban_words:
            message: str
            if len(ban_words) == 1:
                message = "Слово " + ", ".join(ban_words) + " добавлено в список запрещенных слов"
            else:
                message = "Слова: " + ", ".join(ban_words) + " добавлены в список запрещенных слов"
            reply(data, message=message)
        else:
            reply(data, message="Слово уже в списке запрещенных слов")

    @client.command(["get_banword", "gbw", "получить_банворд", "пбв"], condition=in_staff)
    def get_ban_word(data: Parameters):
        ban_words = ", ".join(banned_words)
        logger.info(ban_words)
        message = f"Список запрещенных слов:\n {ban_words}"
        data.subClient.send_message(chatId=data.chatId, message=message, replyTo=data.messageId)

    @client.command(["remove_banword", "rbw", "убрать_банворд", "убв"], condition=in_staff)
    def remove_ban_word(data: Parameters):
        ban_words = data.message.split()
        for ban_word in ban_words:
            if ban_word.lower() in banned_words:
                banned_words.remove(ban_word.lower())
            else:
                ban_words.remove(ban_word)

        with open("utilities\\banned_words.txt", "w", encoding="utf-16") as file:
            for ban_word in banned_words:
                file.write(ban_word + "\n")

        if ban_words:
            if len(ban_words) == 1:
                message = f"Слово {', '.join(ban_words)} убрано из списка запрещенных слов"
            else:
                message = f"Слова: {', '.join(ban_words)} убраны из списка запрещенных слов"
            data.subClient.send_message(chatId=data.chatId, message=message, replyTo=data.messageId)
        else:
            data.subClient.send_message(chatId=data.chatId, message="Слова нет в списке запрещенных слов",
                                        replyTo=data.messageId)

    @client.command(["ban_word_mode", "bwm", "убрать_банворды", "убвы"], condition=in_staff)
    def set_ban_word_mode(data: Parameters):
        content = str(data.message)
        if content == "on":
            if len(banned_words):
                reply(data, "Банворд уже система работает")
            else:
                reply(data, "Банворд система включена")
                with open("utilities\\banned_words.txt", "w", encoding="utf-16") as fbw, \
                        open("utilities\\bw.txt", "r", encoding="utf-16") as fb:
                    for word in fb:
                        fbw.write(word)
                        banned_words.add(word.strip())
        elif content == "off":
            if len(banned_words):
                reply(data, "Запрещенные слова убраны")
                banned_words.clear()
                with open("utilities\\bw.txt", "w", encoding="utf-16") as fb, \
                        open("utilities\\banned_words.txt", "r", encoding="utf-16") as fbw:
                    for word in fbw:
                        fb.write(word)
                fb = open("utilities\\banned_words.txt", "w", encoding="utf-16")
                fb.close()
            else:
                reply(data, "Список запрещенных слов пуст")
        else:
            reply(data, "Вы ничего не ввели в команду")

    @client.answer(["слышь", "эй"], condition=is_agent)
    def pidr(data: Parameters):
        user_id = data.replyUserId
        default = "педик"
        user_dict = {
            get_id_from_code("e9kwk3"): "шлюха",
            get_id_from_code("dxmnws"): "гандон",
            get_id_from_code("2jcf0f"): "даун"
        }
        data.subClient.send_message(chatId=data.chatId, message=f"‎‏‎‏@{user_dict.get(user_id, default)}‬‭!",
                                    mentionUserIds=[user_id])

    @client.command(["check_wall_comments", "cwc"], condition=is_agent)
    def check_wall_comments(data: Parameters):
        user_id = get_id_from_code(data.message)
        data.subClient.get_wall_comments(userId=user_id, sorting="newest", size=50)

    # TODO: moderation_history
    @client.command(["get_moderation_history", "gmh"], condition=in_staff)
    def get_moderation_history(data: Parameters, user_link: str, size: int = 20):
        user_id = get_id_from_code(user_link)
        translation = {
            'Issued Strike to Member': 'Режим Чтения',
            'Unbanned Member': 'Участник Разбанен',
            'Banned Member': 'Участник Забанен',
            'Removed Curator': 'Куратор Убран',
            'Promote Curator Accepted': 'Заявка на Куратора Принята',
            'Promoted a Curator': 'Назначение Куратором',
            'Un-Hid Member Profile': 'Показать Профиль Участника',
            'Hid Member Profile': 'Скрытие Профиля Участника',
            'Edited Member Title': 'Звание Участника',
            'Promote Agent Accepted': 'Заявка на Агента Принята',
            'Promoted an Agent': 'Назначение Агентом',
            'Issued Warning to Member': 'Предупреждение Участнику',
            'Promote Leader Accepted': 'Заявка на Лидера Принята',
            'Promoted a Leader': 'Назначение Лидером'
        }
        unusual_nicknames = {
            'System': 'Команда Амино',
            '-': 'Удаленный Аккаунт'
        }
        messages = []
        adm_log = data.subClient.moderation_history(userId=user_id, size=size)
        for num, nickname, created_time, operation_name, content in zip(enumerate(adm_log.author.nickname, start=1),
                                                                        adm_log.author.nickname,
                                                                        adm_log.createdTime,
                                                                        adm_log.operationName,
                                                                        adm_log.operationDetail):
            operation_name = translation.get(operation_name, operation_name)
            created_time = (' '.join(created_time.split('T')))[:-1]
            nickname = unusual_nicknames.get(nickname, nickname)
            content = '' if content is None else content
            messages.append(f'''\
Операция {num[0]}:
Название операции: {operation_name}
Время создания: {created_time}
Автор операции: {nickname}
Детали операции: {content}

''')
        max_size = 2000
        message = ''
        for msg in messages:
            if len(msg) + len(message) < max_size:
                message += msg
                continue
            reply(data, message)
            time.sleep(2)
            message = msg
        if message:
            reply(data, message)

    @client.command(["copy_bubble", "cb"], condition=is_agent)
    def copy_bubble(data: Parameters):
        message_id = data.replyId
        for chat_id in holy_chats:
            data.subClient.copy_bubble(chatId=chat_id, replyId=message_id)

    @client.command(["change_nickname", "cn"], condition=is_agent)
    def change_nickname(data: Parameters):
        data.subClient.edit_profile(nickname=data.message)
        reply(data, "Никнейм изменен")

    @client.command(["change_bio", "cb"], condition=is_agent)
    def change_bio(data: Parameters):
        data.subClient.edit_profile(content=data.message)
        reply(data, "Статус изменен")

    @client.command(["change_icon", "ci"], condition=is_agent)
    def change_icon(data: Parameters):
        filename = data.message
        try:
            with open(file=f"icon\\{filename}.jpg", mode="rb") as file_img:
                data.subClient.edit_profile(icon=file_img)
            reply(data, "Иконка изменена")
        except Exception as e:
            logger.warning(repr(e))
            reply(data, "Ошибка")

    @client.command(["change_background", "cbg"], condition=is_agent)
    def change_background(data: Parameters):
        filelink = data.message
        data.subClient.edit_profile(backgroundImage=filelink)

    @client.command(["help_adm", "хелп_адм", "помощь_адм", "ha", "ха"], condition=in_staff)
    def help_adm(data: Parameters):
        help_admin = []
        full_help = ''
        with open("utilities\\help_admin.txt", "r", encoding="utf-8") as f:
            for text_line in f:
                help_admin.append(text_line.strip())
                if text_line.strip().startswith("[b]") or text_line.strip().startswith("[cb]"):
                    full_help += text_line

        help_dict = {
            "ban": f"{help_admin[2]}\n{help_admin[3]}\n{help_admin[4]}\n{help_admin[5]}\n{help_admin[6]}",
            "бан": f"{help_admin[2]}\n{help_admin[3]}\n{help_admin[4]}\n{help_admin[5]}\n{help_admin[6]}",
            "unban": f"{help_admin[7]}\n{help_admin[8]}\n{help_admin[9]}",
            "разбан": f"{help_admin[7]}\n{help_admin[8]}\n{help_admin[9]}",
            "анбан": f"{help_admin[7]}\n{help_admin[8]}\n{help_admin[9]}",
            "kick": f"{help_admin[10]}\n{help_admin[11]}\n{help_admin[12]}\n{help_admin[13]}\n{help_admin[14]}\n{help_admin[15]}",
            "invite_to_chat": f"{help_admin[16]}\n{help_admin[17]}\n{help_admin[18]}",
            "itc": f"{help_admin[16]}\n{help_admin[17]}\n{help_admin[18]}",
            "join": help_admin[19],
            "check_users": f"{help_admin[20]}",
            "cu": f"{help_admin[20]}",
            "banlist": help_admin[21],
            "кик": help_admin[22],
            "get_nickname": f"{help_admin[23]}\n{help_admin[24]}\n{help_admin[25]}",
            "gn": f"{help_admin[23]}\n{help_admin[24]}\n{help_admin[25]}",
            "add_user_to_banlist": f"{help_admin[26]}\n{help_admin[27]}\n{help_admin[28]}",
            "add_to_banlist": f"{help_admin[26]}\n{help_admin[27]}\n{help_admin[28]}",
            "atb": f"{help_admin[26]}\n{help_admin[27]}\n{help_admin[28]}",
            "autb": f"{help_admin[29]}\n{help_admin[30]}\n{help_admin[31]}",
            "remove_user_from_banlist": f"{help_admin[32]}\n{help_admin[33]}\n{help_admin[34]}",
            "remove_from_banlist": f"{help_admin[32]}\n{help_admin[33]}\n{help_admin[34]}",
            "rem_from_banlist": f"{help_admin[32]}\n{help_admin[33]}\n{help_admin[34]}",
            "rfb": f"{help_admin[32]}\n{help_admin[33]}\n{help_admin[34]}",
            "rufb": f"{help_admin[35]}\n{help_admin[36]}\n{help_admin[37]}",
            "at": f"{help_admin[38]}\n{help_admin[39]}\n{help_admin[40]}",
            "add_title": f"{help_admin[38]}\n{help_admin[39]}\n{help_admin[40]}",
            "дать_звание": f"{help_admin[38]}\n{help_admin[39]}\n{help_admin[40]}",
            "remove_title": f"{help_admin[41]}\n{help_admin[42]}\n{help_admin[43]}",
            "rt": f"{help_admin[41]}\n{help_admin[42]}\n{help_admin[43]}",
            "убрать_звание": f"{help_admin[41]}\n{help_admin[42]}\n{help_admin[43]}",
            "strike": f"{help_admin[44]}\n{help_admin[45]}\n{help_admin[46]}",
            "st": f"{help_admin[44]}\n{help_admin[45]}\n{help_admin[46]}",
            "режим_чтения": f"{help_admin[44]}\n{help_admin[45]}\n{help_admin[46]}",
            "рч": f"{help_admin[44]}\n{help_admin[45]}\n{help_admin[46]}"
            }
        try:
            reply(data, help_dict.get(data.message, full_help))
            if data.message in ["at", "add_title", "дать_звание"]:
                with open("utilities\\hex_colors.jpg", "rb") as file:
                    data.subClient.send_message(chatId=data.chatId, fileType="image", file=file)
        except Exception as e:
            logger.warning(repr(e))
            reply(data, "Неправильно введена команда")

    @client.command(["help", "хелп", "помощь"])
    def help_user(data: Parameters):
        hlp_user = []
        full_help = ''
        with open("utilities\\help_user.txt", "r", encoding="utf-8") as f:
            for text_line in f:
                hlp_user.append(text_line.strip())
                if text_line.strip().startswith("[b]") or text_line.strip().startswith("[cb]"):
                    full_help += text_line.strip()
        reply(data, full_help)

    def _get_nickname(data: Parameters):
        content = str(data.message).split()
        nicknames = []
        for user_link in content:
            user_id = get_id_from_code(user_link)
            nickname = data.subClient.get_user_info(user_id).nickname
            nicknames.append(nickname)
        return nicknames

    @client.command(["get_nickname", "gn"], condition=in_staff)
    def get_nickname(data: Parameters):
        nicknames = _get_nickname(data)
        reply(data, ", ".join(nicknames))

    def _add_user_to_banlist(data: Parameters, nickname: str):
        if is_reporter(data) or in_staff(data):
            if nickname in banlist:
                reply(data, f"{nickname} уже в списке запрещенных ников")
            else:
                banlist.add(nickname)
                with open(banfile, 'a', encoding='utf-16', errors='surrogateescape') as f:
                    f.write(nickname + '\n')
                reply(data, f"{nickname} добавлен в список запрещенных ников")

    @client.command("autb", condition=in_staff)
    def autb(data: Parameters):
        nicknames = _get_nickname(data)
        for nick in nicknames:
            _add_user_to_banlist(data, nickname=nick)

    @client.command(["add_user_to_banlist", "add_to_banlist", "atb"])
    def add_user_to_banlist(data: Parameters):
        nicknames = str(data.message).split(", ")
        for nick in nicknames:
            if nick == '' or nick == ' ':
                continue
            _add_user_to_banlist(data, nickname=nick)

    def _remove_user_from_banlist(data: Parameters, nickname: str):
        if in_staff(data) or is_reporter(data):
            if nickname in banlist:
                banlist.remove(nickname)
                with open(banfile, 'w', encoding='utf-16', errors='surrogateescape') as f:
                    for banlistUser in banlist:
                        f.write(banlistUser + '\n')
                reply(data, f"{nickname} убран из списка запрещенных ников")
            else:
                reply(data, f"{nickname} нет в списке запрещенных ников")

    @client.command("rufb", condition=in_staff)
    def rufb(data: Parameters):
        nicknames = _get_nickname(data)
        for nick in nicknames:
            _remove_user_from_banlist(data, nickname=nick)

    @client.command(["remove_user_from_banlist", "remove_from_banlist", "rem_from_banlist", "rfb"])
    def remove_user_from_banlist(data: Parameters):
        nicknames = str(data.message).split(", ")
        print(nicknames)
        for nick in nicknames:
            if nick == '' or nick == ' ':
                continue
            _remove_user_from_banlist(data, nickname=nick)

    def _ban(data: Parameters, user_id: str, nickname: str):
        current_time = get_current_time()
        if not data.subClient.is_in_staff(user_id):
            message_list = data.subClient.get_chat_messages(chatId=data.chatId, size=50)
            for uid, message_id in zip(message_list.author.userId, message_list.messageId):
                if uid != user_id:
                    continue
                data.subClient.delete_message(chatId=data.chatId, messageId=message_id, asStaff=True,
                                              reason=f'{current_time} {nickname} был забанен')
            data.subClient.ban(userId=user_id, reason=f"{current_time} {nickname} получил бан от {data.author}")
            reply(data, f"Пользователь забанен")
        else:
            reply(data, "Нельзя забанить пользователя из админки")

    @client.command(["ban", "бан"], condition=in_staff)
    def ban(data: Parameters):
        content = data.message
        if str(content) == "":
            try:
                uid = data.replyUserId
                nickname = data.replyAuthor
                _ban(data, user_id=uid, nickname=nickname)
            except Exception as e:
                logger.warning(repr(e))
                reply(data, "Вы не ввели ник или же не реплайнули пользователя")
        else:
            try:
                links = content.split()
                for link in links:
                    user_id = get_id_from_code(link)
                    nickname = data.subClient.get_user_info(user_id).nickname
                    _ban(data, user_id=user_id, nickname=nickname)
            except Exception as e:
                logger.warning(repr(e))
                userIds = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
                for user_id in userIds:
                    nickname = data.subClient.get_user_info(user_id).nickname
                    _ban(data, user_id=user_id, nickname=nickname)

    def _unban(data: Parameters, user_id: str, nickname: str):
        current_time = get_current_time()
        data.subClient.unban(userId=user_id, reason=f"{current_time} {nickname} получил разбан от {data.author}")
        reply(data, "Пользователь разбанен")

    @client.command(["разбан", "unban", "анбан"], condition=in_staff)
    def unban(data: Parameters):
        content = data.message
        if str(content) == "":
            try:
                uid = data.replyUserId
                nickname = data.replyAuthor
                _unban(data, user_id=uid, nickname=nickname)
            except Exception as e:
                logger.warning(repr(e))
                reply(data, "Вы не ввели ник или же не реплайнули пользователя")
        else:
            try:
                links = content.split()
                for link in links:
                    user_id = get_id_from_code(link)
                    nickname = data.subClient.get_user_info(user_id).nickname
                    _unban(data, user_id=user_id, nickname=nickname)
            except Exception as e:
                logger.warning(repr(e))
                user_ids = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
                for user_id in user_ids:
                    nickname = data.subClient.get_user_info(user_id).nickname
                    _unban(data, user_id=user_id, nickname=nickname)

    def _kick(data: Parameters, user_id: str):
        current_time = get_current_time()
        if not data.subClient.is_in_staff(user_id):
            message_list = data.subClient.get_chat_messages(chatId=data.chatId, size=100)
            for uid, message_id, nickname in zip(message_list.author.userId,
                                                 message_list.messageId, message_list.author.nickname):
                if uid != user_id:
                    continue
                data.subClient.delete_message(chatId=data.chatId, messageId=message_id, asStaff=True,
                                              reason=f'{current_time} {nickname} был кикнут')
            data.subClient.kick(chatId=data.chatId, userId=user_id, allowRejoin=False)
            reply(data, "Пользователь кикнут")
        else:
            reply(data, "Нельзя кикнуть пользователя из админки")

    @client.command(["kick", "кик"], condition=in_staff)
    def kick(data: Parameters):
        content = str(data.message)
        if content == "":
            try:
                uid = data.replyUserId
                _kick(data, user_id=uid)
            except Exception as e:
                logger.warning(repr(e))
                reply(data, "Вы не ввели ник или же не реплайнули пользователя")
        else:
            try:
                links = content.split()
                for link in links:
                    user_id = get_id_from_code(link)
                    _kick(data, user_id=user_id)
            except Exception as e:
                logger.warning(repr(e))
                user_ids = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
                for user_id in user_ids:
                    _kick(data, user_id=user_id)

    @client.command(["strike", "st", "режим_чтения", "рч"], condition=in_staff)
    def strike(data: Parameters, time_for: str, user_link: str = None):
        user_id = data.replyUserId if user_link is None else get_id_from_code(user_link)
        dict_time = {
            '1': 3600,
            '3': 10800,
            '6': 21600,
            '12': 43200,
            '24': 86400
        }
        str_time = {
            '1': 'один час',
            '3': 'три часа',
            '6': 'шесть часов',
            '12': 'двенадцать часов',
            '24': 'один день'
        }
        time_amount = dict_time.get(time_for, 3600)
        nickname = data.subClient.get_user_info(user_id).nickname
        reason = f"{nickname} получил страйк от {data.author} на {str_time.get(time_for, 'один час')}"
        if not data.subClient.is_in_staff(user_id):
            data.subClient.strike(userId=user_id, time=time_amount, title="Spamming", reason=reason)
            reply(data, f"{nickname} получил страйк на {str_time.get(time_for, 'один час')}")
        else:
            reply(data, "Нельзя выдать режим чтения пользователю из админки")

    @client.command(['hide_chat', 'hc'], condition=reporter_or_staff)
    def hide_chat(data: Parameters, chat_link: str = None):
        if chat_link is None:
            chat_id = data.chatId
        else:
            chat_id = get_id_from_code(chat_link)
        thread = data.subClient.get_chat_thread(chatId=chat_id)
        chat_name = thread.title
        data.subClient.hide(chatId=chat_id, reason=f"{data.author} скрыл чат {chat_name}")
        logger.info(f"{chat_name} чат скрыт")

    @client.command(['id_hide'], condition=is_reporter)
    def id_hide(data: Parameters, chat_id: str):
        data.subClient.hide(chatId=chat_id, reason="Спам чат обнаружен")

    @client.command(['id_kick'], condition=is_reporter)
    def id_kick(data: Parameters, chat_id: str, user_id: str):
        data.subClient.kick(chatId=chat_id, userId=user_id, allowRejoin=True)

    @client.command("id_ban", condition=is_reporter)
    def ban_id(data: Parameters):
        current_time = get_current_time()
        content = str(data.message).split()
        user_id = content[0]
        content = content[1:]
        nickname = " ".join(content)
        data.subClient.ban(userId=user_id, reason=f"{current_time} {nickname} спамил ссылками в лс.")
        reply(data, f"Пользователь {nickname} забанен")

    @client.command("id_unban", condition=is_reporter)
    def unban_id(data: Parameters):
        current_time = get_current_time()
        content = str(data.message).split()
        user_id = content[0]
        content = content[1:]
        nickname = " ".join(content)
        data.subClient.unban(userId=user_id, reason=f"{current_time} {nickname} прощен за спам")
        reply(data, f"Пользователь {nickname} разбанен")

    @client.command(["transfer_host", "th"], condition=is_reporter)
    def transfer_host(data: Parameters):
        data.subClient.transfer_host(chatId=data.message, userIds=[bot_id])

    @client.command("join_chat", condition=is_reporter)
    def join_chat(data: Parameters):
        try:
            data.subClient.join_chat(chatId=data.message)
        except Exception as e:
            logger.warning(repr(e))
            print("can't join chat")

    @client.command(["add_color", "ac", "добавить_цвет", "дц"])
    def add_color(data: Parameters, color_name: str, hex_code: str):
        if hex_code[0] == "#":
            with open("utilities\\hex_colors.txt", "a", encoding="utf-8") as f:
                f.write(f"{color_name} {hex_code.upper()}\n")
            reply(data, f"Цвет {color_name} добавлен")
        else:
            reply(data, "Неправильно введен код цвета")

    @client.command(["add_title", "at", "дать_звание"], condition=in_staff)
    def add_title(data: Parameters):
        content = data.message.split()
        user_link = content[0]
        color = content[1]
        if color[0] != '#':
            color = hex_colors.get(color.lower(), "#000000")
        content = content[2:]
        title = ' '.join(content)
        user_id = get_id_from_code(user_link)
        try:
            data.subClient.add_title(uid=user_id, title=title, color=color)
            reply(data, "Звание назначено")
        except ReachedTitleLength:
            logger.info(repr(ReachedTitleLength))
            reply(message="Максимальная длина звания 20 символов")
        except ReachedMaxTitles:
            logger.info(repr(ReachedMaxTitles))
            reply(data, "Количество званий достигло максимума")
        except AccessDenied:
            logger.info(repr(AccessDenied))
            reply(data, "Цвет введен неправильно")
        except Exception as e:
            logger.warning(repr(e))
            reply(data, "Ошибка")

    @client.command(["remove_title", "rt", "убрать_звание"], condition=in_staff)
    def remove_title(data: Parameters):
        try:
            content = data.message.split()
            user_link = content[0]
            title = content[1:]
            user_id = get_id_from_code(user_link)
            data.subClient.remove_title(uid=user_id, title=" ".join(title))
            reply(data, "Звание убрано")
        except IndexError:
            logger.info(repr(IndexError))
            reply(data, "Не введено звание")

    @client.command(["invite_to_chat", "itc"], condition=in_staff)
    def invite_to_chat(data: Parameters, user_link: str, chat_link: str):
        user_id = get_id_from_code(user_link)
        chat_id = get_id_from_code(chat_link)
        nickname = data.subClient.get_user_info(userId=user_id).nickname
        data.subClient.invite_to_chat(userId=user_id, chatId=chat_id)
        reply(data, f"{nickname} приглашен в чат")

    @client.command("delete_message", condition=is_reporter)
    def delete_message(data: Parameters, chat_id: str, message_id: str):
        data.subClient.delete_message(chatId=chat_id, messageId=message_id, asStaff=True,
                                      reason=f'{data.author} нашел спам ссылкой')

    @client.command(["get_info", "gi"], condition=is_agent)
    def get_message_info(data: Parameters):
        message_info = data.subClient.get_message_info(chatId=data.chatId, messageId=data.replyId)

    @client.command("chatId", condition=in_staff)
    def get_cid(data: Parameters):
        print(data.chatId)

    @client.command(["get_user_id", "gui"], condition=in_staff)
    def get_user_id(data: Parameters):
        user_id = get_id_from_code(data.message)
        print(user_id)
        reply(data,user_id)

    @client.command(["get_chat_id", "gci"], condition=in_staff)
    def get_chat_id(data: Parameters):
        chat_id = get_id_from_code(data.message) if data.message else data.chatId
        print(chat_id)
        reply(data, chat_id)

    @client.command(condition=in_staff)
    def join(data: Parameters):
        data.subClient.join_all_chat()
        reply(data, "all chat joined")

    @client.command(["clear"], condition=in_staff)
    def clear(data: Parameters, size: int = 100):
        message_list = data.subClient.get_chat_messages(chatId=data.chatId, size=size)
        for user_id, message_id, message_type in zip(message_list.author.userId,
                                                     message_list.messageId, message_list.type):
            if message_type == TEXT or message_type == STICKER or message_type == VOICE:
                continue
            data.subClient.delete_message(chatId=data.chatId, messageId=message_id, asStaff=True,
                                          reason=f'Чистка сообщений')
            # time.sleep(2)
        data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId, asStaff=True,
                                      reason=f'Команда исполнена')

    @client.command(["clear_messages", "cmsg"], condition=in_staff)
    def clear_messages(data: Parameters, size: int = 50):
        uid = data.replyUserId
        if uid and not data.subClient.is_in_staff(uid):
            for chat_id in general_chats:
                message_list = data.subClient.get_chat_messages(chatId=chat_id, size=size)
                for user_id, message_id in zip(message_list.author.userId, message_list.messageId):
                    if uid != user_id:
                        continue
                    data.subClient.delete_message(chatId=chat_id, messageId=message_id, asStaff=True,
                                                  reason='Чистка сообщений')
            data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId)
        else:
            reply(data, "Нельзя очистить сообщения от пользователя из админки")

    @client.command(["clear_chats", "cc"], condition=is_reporter)
    def clear_chats(data: Parameters, chat_id: str, uid: str):
        t = time.localtime()
        user_list = client.get_chat_users(chatId=chat_id, size=100)
        nickname = ""
        for user_id, nick in zip(user_list.userId, user_list.nickname):
            if user_id == bot_id:
                continue
            if user_id == uid:
                nickname = nick
            try:
                data.subClient.kick(chatId=chat_id, userId=user_id, allowRejoin=False)
            except Exception as e:
                logger.warning(repr(e))
            time.sleep(20)
        reason = f'{((t.tm_hour - 2) % 24):0>2}:{t.tm_min:0>2}:{t.tm_sec:0>2} {nickname} спамил ссылками в лс'
        data.subClient.ban(userId=uid, reason=reason)

    @client.command(["clear_chat", "cc"], condition=in_staff)
    def clear_chat(data: Parameters, user_link: str = "", chat_link: str = ""):
        t = time.localtime()
        chat_id = get_id_from_code(chat_link) if chat_link else data.chatId
        uid = get_id_from_code(user_link) if user_link else data.replyUserId
        user_list = client.get_chat_users(chatId=chat_id, size=100)
        nickname = ""
        for user_id, nick in zip(user_list.userId, user_list.nickname):
            if user_id == bot_id:
                continue
            if user_id == uid:
                nickname = nick
            try:
                data.subClient.kick(chatId=chat_id, userId=user_id, allowRejoin=False)
            except Exception as e:
                logger.warning(repr(e))
            time.sleep(20)
        reason = f'{((t.tm_hour - 2) % 24):0>2}:{t.tm_min:0>2}:{t.tm_sec:0>2} {nickname} спамил ссылками в лс'
        data.subClient.ban(userId=uid, reason=reason)

    @client.command(["transfer_host", "th"], condition=in_staff)
    def transfer_host(data: Parameters, chat_link: str = "", user_link: str = ""):
        update_deviceId(client.device_id)
        chat_id = get_id_from_code(chat_link) if chat_link else data.chatId
        user_id = get_id_from_code(user_link) if user_link else client.userId
        status_code = data.subClient.transfer_host(chatId=chat_id, userIds=[user_id])
        print(f"{status_code=}")
        request_id = data.subClient.get_chat_thread(chatId=chat_id).organizerTransferId
        print(f"{request_id=}")
        # request_id = data.subClient.get_user_info(userId=user_id).requestId
        # print(f"{request_id=}")
        data.subClient.accept_host(chatId=chat_id, requestId=request_id)
        logger.info("host is transfered to bot")

    @client.command(["delete_chat", "dch"], condition=in_staff)
    def delete_chat(data: Parameters, chat_link: str = ""):
        chat_id = get_id_from_code(chat_link) if chat_link else data.chatId
        data.subClient.transfer_host(chatId=chat_id, userIds=[client.userId])
        request_id = data.subClient.get_chat_thread(chatId=chat_id).organizerTransferId
        data.subClient.accept_host(chatId=chat_id, requestId=request_id)
        data.subClient.delete_chat(chatId=chat_id)
        logger.info("chat deleted")

    @client.command(["add_ban_pic", "abp"], condition=in_staff)
    def add_ban_picture(data: Parameters, user_link: str):
        user_id = get_id_from_code(user_link)
        user_icon = data.subClient.get_user_info(user_id).icon
        num = len(os.listdir('utilities\\ban_icons'))
        h = httplib2.Http('.cache')
        response, content = h.request(user_icon)
        with open(f'utilities\\ban_icons\\ban_icon{num}.jpg', 'wb') as f:
            f.write(content)
        data.subClient.send_message(chatId=data.chatId, message="Картинка добавлена")

    @client.command(['add_nsfw_pic', 'anp'], condition=in_staff)
    def add_nsfw_pic(data: Parameters, user_link: str = None):
        user_id = data.replyUserId if user_link is None else get_id_from_code(user_link)
        user_icon = data.subClient.get_user_info(user_id).icon
        num = len(os.listdir('utilities\\nsfw_icons'))
        h = httplib2.Http('.cache')
        response, content = h.request(user_icon)
        with open(f'utilities\\nsfw_icons\\nsfw_icon{num}.jpg', 'wb') as f:
            f.write(content)
        reply(data, "Картинка добавлена")

    @client.command(["check_users", "cu"])
    def check_users(data: Parameters, size: int = 100):
        current_time = get_current_time()
        count_user = 0
        upl = data.subClient.get_all_users(start=0, size=size, type="recent").profile
        for nickname, user_id, bio, icon in zip(upl.nickname, upl.userId, upl.content, upl.icon):

            if icon is None:
                data.subClient.ban(userId=user_id, reason=f"{current_time} {nickname} с пустой иконкой")
                logger.info(f"Пойман пользователь с пустой иконкой {nickname}")
                count_user += 1
                continue

            flag = False

            h = httplib2.Http('.cache')
            response, content = h.request(icon)
            try:
                with open('utilities\\img.jpg', 'wb') as f:
                    f.write(content)
                with Image.open('utilities\\img.jpg') as user_icon:
                    for filename in os.listdir('utilities\\ban_icons'):
                        with Image.open(f"utilities\\ban_icons\\{filename}") as ban_icon:
                            size = 256, 256
                            user_icon.thumbnail(size)
                            ban_icon.thumbnail(size)
                            if hash(user_icon.tobytes()) != hash(ban_icon.tobytes()):
                                continue
                            data.subClient.ban(userId=user_id, reason=f"{current_time} {nickname} запрещенный пользователь")
                            logger.info(f"Найдена запрещенная иконка {nickname}")
                            count_user += 1
                            flag = True
                            break

                    for filename in os.listdir('utilities\\nsfw_icons'):
                        with Image.open(f"utilities\\nsfw_icons\\{filename}") as nsfw_icon:
                            size = 256, 256
                            user_icon.thumbnail(size)
                            nsfw_icon.thumbnail(size)
                            if hash(user_icon.tobytes()) != hash(nsfw_icon.tobytes()):
                                continue
                            data.subClient.hide(userId=user_id, reason=f"{current_time} {nickname} иконка против правил")
                            logger.info(f"Найдена нежелательная иконка {nickname}")
            except UnidentifiedImageError:
                data.subClient.ban(userId=user_id, reason=f"{current_time} {nickname} с пустой иконкой")
                logger.info(f"Пойман пользователь с пустой иконкой {nickname}")
                count_user += 1
                continue

            if flag:
                continue

            link = detect_link(bio) if bio else ""
            if link and "aminoapps.com/p/" not in link and "aminoapps.com/u/" not in link:
                data.subClient.ban(userId=user_id, reason=f"{current_time} {nickname} рекламит в статусе: {link}")
                logger.info(f"{nickname} пойман за рекламой")
                count_user += 1
                continue

            if nickname not in banlist:
                continue

            reason = f"{current_time} Пойман пользователь из банлиста: {nickname}"
            data.subClient.ban(userId=user_id, reason=reason)
            count_user += 1
            logger.info(f"{nickname} пойман, его айди : {user_id}")
        data.subClient.send_message(chatId=data.chatId, message=f"Забанено {count_user} пользователей")

    @client.command(["check_profile"], condition=in_staff)
    def check_profile(data: Parameters, user_link: str):
        current_time = get_current_time()
        user_id = get_id_from_code(user_link)
        user_profile = data.subClient.get_user_info(user_id)
        user_icon = user_profile.icon
        print(user_icon)
        nickname = user_profile.nickname
        bio = user_profile.content
        link = detect_link(bio) if bio else ""
        if link and "aminoapps.com/p/" not in link:
            data.subClient.ban(userId=user_id, reason=f"{current_time} {nickname} рекламит в биографии: {link}")
            reply(data, f"{nickname} забанен")

    @client.command(["unban_users", "uu"], condition=in_staff)
    def unban_users(data: Parameters, size: int = 100):
        user_profile_list = data.subClient.get_all_users(start=0, size=size, type="banned").profile
        for user_id, nickname in zip(user_profile_list.userId, user_profile_list.nickname):
            try:
                data.subClient.unban(userId=user_id, reason=f"{nickname} Был забанен по ошибке")
            except Exception as e:
                logger.warning(repr(e))
        reply(data, f"Разбанено {size} пользователей")

    def get_ban_list():
        ban_list = "[c]Список запрещенных ников:\n[b]"
        ban_list += ", ".join(banlist)
        return ban_list + "."

    @client.command(["ban_list", "bl"], condition=in_staff)
    def show_ban_list(data: Parameters):
        ban_list = get_ban_list()
        reply(data, ban_list)

    # @client.command(["download_song", "ds", "загрузить_песню", "зп"], condition=in_staff)
    # def download_song(data: Parameters):
    #     content = data.message.split(' ')
    #     download_mp3(content)

    @client.command(["play", "p", "п", "плей"])
    def send_audio_message(data: Parameters):
        try:
            if str(data.message).lower() in ["список", "лист", "list"]:
                music_list = "[c]Список добавленных аудиофайлов:\n[b]"
                for filename in os.listdir("music"):
                    music_list += filename[:-4] + ', '
                reply(data, music_list[:-2])
            else:
                with open(f"music\\{str(data.message).lower()}.mp3", "rb") as file_mp:
                    data.subClient.send_message(chatId=data.chatId, messageType=2, file=file_mp, fileType="audio")
        except FileNotFoundError:
            logger.warning(repr(FileNotFoundError))
            with open(f"music\\{str(data.message).lower()}.wav", "rb") as file_mp:
                data.subClient.send_message(chatId=data.chatId, messageType=2, file=file_mp, fileType="audio")
            reply(data, "Нет аудиофайла с таким названием")
        except InvalidRequest:
            logger.warning(repr(InvalidRequest))
            reply(data, "Ошибка")

    @client.command(["мама"])
    def mama(data: Parameters):
        name = f", {data.message}," if data.message else ""
        text = f'''\
И твою маму шлюху ебу я целый день.
Она сосала хуй мой - сосать ведь ей не лень. 
Огромный мой дрожащий член сосёт она с улыбкой.
Доверить{name} маму мне то было ведь ошибкой.\
'''
        data.subClient.send_message(chatId=data.chatId, message=text)

    @client.command(["add_kick_stick", "aks"])
    def add_kick_stick_id(data: Parameters):
        stick_id = data.replyStickerId
        if stick_id:
            kick_stick_ids.add(stick_id)

    @client.answer("футбольчик")
    def ans(data: Parameters):
        data.subClient.send_message(chatId=data.chatId, message="мальчики походят на качков")
        data.subClient.send_message(chatId=data.chatId, message="игра в ножички плавно переходит на улицу")

    @client.answer(["Че сутулишься", "чё сутулишься", "че сутулишся"])
    def an(data):
        data.subClient.send_message(chatId=data.chatId, message="трапеция норм")
        data.subClient.send_message(chatId=data.chatId, message="отработал в спаринге в братаном")

    @client.answer(["кик", "kick"], condition=in_staff)
    def answer_kick(data: Parameters):
        uid = data.replyUserId
        if uid and not data.subClient.is_in_staff(uid):
            data.subClient.kick(chatId=data.chatId, userId=uid, allowRejoin=True)
            reply(data, "Пользователь кикнут")

    @client.answer(
        ["запрет", "говно", "херня", "залупа", "хуета", "убери это", "иди нах", "пососи", "убери", "мда", "мда уж"],
        condition=in_staff)
    def add_to_delete_sticks(data: Parameters):
        stick_id = data.replyStickerId
        if stick_id:
            delete_stick_ids.add(stick_id)

    @client.command(["clear_delete", "cd"], condition=in_staff)
    def clear_delete_stick(data: Parameters):
        delete_stick_ids.clear()
        reply(data, "Список стикеров очищен")

    @client.answer(["лох", "лошок", "лошара"], condition=in_staff)
    def add_to_loh_set(data: Parameters):
        uid = data.replyUserId
        if uid:
            loh_set.add(uid)

    @client.command(["clear_loh", "cl"], condition=in_staff)
    def clear_loh_set(data: Parameters):
        loh_set.clear()
        reply(data, "Список лохов очищен")

    @client.answer(["погнали", "let's go", "les go", "летс гоу", "лес го", "это оно", "вот оно"], condition=in_staff)
    def add_to_kick_stick(data: Parameters):
        stick_id = data.replyStickerId
        if stick_id:
            kick_stick_ids.add(stick_id)

    @client.answer(["тролл", "troll", "затрол"], condition=in_staff)
    def add_to_dict(data: Parameters):
        stick_id = data.replyStickerId
        uid = data.replyUserId
        if stick_id:
            troll_dict[stick_id] = uid

    @client.command(["clear_troll", "ct"], condition=in_staff)
    def clear_troll_dict(data: Parameters):
        troll_dict.clear()
        reply(data, "Словарь для тролл очищен")

    @client.command(["trolling"], condition=is_agent)
    def troll_on(data: Parameters):
        global troll_flag
        troll_flag = False if troll_flag else True
        if troll_flag:
            reply(data, "little bit of trolling")
        else:
            reply(data, "trolling is off")

    @client.on_member_join_chat()
    def on_join(data: Parameters):
        t = time.localtime()
        nickname = data.author
        reason = f'{((t.tm_hour - 2) % 24):0>2}:{t.tm_min:0>2}:{t.tm_sec:0>2} {nickname} зашел в чат'
        data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId, asStaff=True, reason=reason)
        if nickname in banlist:
            data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)

    @client.on_member_leave_chat()
    def on_leave(data: Parameters):
        t = time.localtime()
        nickname = data.author
        reason = f'{((t.tm_hour - 2) % 24):0>2}:{t.tm_min:0>2}:{t.tm_sec:0>2} Пользователь вышел из чата'
        data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId, asStaff=True, reason=reason)
        if nickname in banlist:
            data.subClient.ban(userId=data.authorId, reason=f'{nickname} запрещенный пользователь')

    def detect_link(m: str) -> str:
        regex_am = r"(aminoapps.[^\s]+)"
        regex_tm = r"(t.me[^\s]+)"
        links_am = re.findall(regex_am, m)
        links_tm = re.findall(regex_tm, m)
        result = links_am if links_am else links_tm
        return result[0] if result else ""

    def has_ban_word(message: str) -> bool:
        for banned_word in banned_words:
            regex = rf"{banned_word}"
            words = re.findall(regex, message.lower())
            if len(words):
                return True
        return False

    @client.on_message()
    def text_message(data: Parameters):
        content = str(data.message)
        link = detect_link(content)
        chat_link = "https://t.me/+QErtJAKemEc1Njdi"
        if has_ban_word(content) and not in_staff(data):
            data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId,
                                          asStaff=True, reason="Запрещенное слово")

        if "t.me/" in link and not client.check(data, 'staff') and link not in chat_link:
            catch_spammer(data, user_id=data.authorId, chat_id=data.chatId, message_id=data.messageId,
                          reason=f"{data.author} скинул ссылку на тг:\n{content}")

        if "aminoapps.com/" in link and "aminoapps.com/p/" not in link \
                and not client.check(data, 'staff') and ("aminoapps.com/c/league-of-legends-ru" not in link):
            catch_spammer(data, user_id=data.authorId, chat_id=data.chatId, message_id=data.messageId,
                          reason=f"{data.author} скинул ссылку на аминосоо:\n{content}")

    @client.command("commands", condition=is_agent)
    def get_commands(data: Parameters):
        commands = client.commands['command']
        reply(data, " ".join(commands))

    @client.on_all()
    def on_message(data: Parameters):
        content = str(data.message)
        mtype = data.info.message.type
        default_types = {GROUP_MEMBER_JOIN, GROUP_MEMBER_LEAVE, CHAT_BACKGROUND_CHANGED, CHAT_TITLE_CHANGED,
                         CHAT_ICON_CHANGED, VOICE_CHAT_START, VIDEO_CHAT_START, AVATAR_CHAT_START,
                         VOICE_CHAT_END, VIDEO_CHAT_END, AVATAR_CHAT_END, CHAT_CONTENT_CHANGED,
                         SCREEN_ROOM_START, SCREEN_ROOM_END, CHAT_HOST_TRANSFERED, TEXT_MESSAGE_FORCE_REMOVED,
                         CHAT_REMOVED_MESSAGE, CHAT_PIN_ANNOUNCEMENT, VOICE_CHAT_PERMISSION_OPEN_TO_EVERYONE,
                         VOICE_CHAT_PERMISSION_INVITED_AND_REQUESTED, VOICE_CHAT_PERMISSION_INVITE_ONLY,
                         CHAT_VIEW_ONLY_ENABLED, CHAT_VIEW_ONLY_DISABLED, CHAT_UNPIN_ANNOUNCEMENT,
                         CHAT_TIPPING_ENABLED, CHAT_TIPPING_DISABLED, TIMESTAMP_MESSAGE, WELCOME_MESSAGE}
        raid_types = {TYPE_USER_SHARE_EXURL, TYPE_USER_SHARE_USER, VIDEO_CHAT_NOT_DECLINED,
                      AVATAR_CHAT_NOT_ANSWERED, AVATAR_CHAT_NOT_CANCELLED, AVATAR_CHAT_NOT_DECLINED,
                      DELETE_MESSAGE}

        stick_id = data.replyStickerId

        if mtype == STICKER:
            if troll_flag and data.authorId in loh_set:
                data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId,
                                              asStaff=True, reason='запретный стик')

            if stick_id in troll_dict.keys():
                data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId,
                                              asStaff=True, reason='troll')
                data.subClient.kick(chatId=data.chatId, userId=troll_dict[stick_id], allowRejoin=True)

            if stick_id in delete_stick_ids:
                data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId,
                                              asStaff=True, reason='запретный стик')
            if stick_id in kick_stick_ids:
                for loh_id in loh_set:
                    data.subClient.kick(chatId=data.chatId, userId=loh_id, allowRejoin=True)

        if mtype in default_types:
            data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId,
                                          asStaff=True, reason='системное сообщение')
            if content != "None":
                link = detect_link(content)
                if ("t.me/" in link) or ("aminoapps.com/" in link):
                    catch_spammer(data, user_id=data.authorId, chat_id=data.chatId, message_id=data.messageId,
                                  reason=f"{data.author} спамит запрещенными ссылками в лс.\n{content}")

        if mtype == CHAT_INVITE and not is_reporter(data):
            link = detect_link(content)
            if ("t.me/" in link) or ("aminoapps.com/" in link):
                data.subClient.join_chat(chatId=data.chatId)
                catch_spammer(data, user_id=data.authorId, chat_id=data.chatId, message_id=data.messageId,
                              reason=f"{data.author} спамит запрещенными ссылками в лс.\n{content}")
                data.subClient.delete_chat(chatId=data.chatId)
            else:
                data.subClient.join_chat(chatId=data.chatId)

        if mtype in raid_types and not is_reporter(data):
            if mtype == DELETE_MESSAGE and content == "None":
                data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId,
                                              asStaff=True, reason='удаленное сообщение')
            else:
                logger.info('raid alert')
                logger.info(f'message Type : {mtype}')
                logger.info(f'message : {content}')
                try:
                    catch_spammer(data, user_id=data.authorId, chat_id=data.chatId, message_id=data.messageId,
                                  reason=f"Тип сообщения {mtype} обнаружен! Никнейм: {data.author} | Id пользователя: {data.authorId} | Id сообщения: {data.messageId}.\nСодержание сообщения: {content}")
                except Exception as e:
                    logger.warning(repr(e))

    client.launch(True)
    # client.single_launch("league-of-legends-ru", True)
    logger.info(f"{client.profile.nickname} ready")


if __name__ == '__main__':
    try:
        main()
    except IpTemporaryBan:
        restart()
