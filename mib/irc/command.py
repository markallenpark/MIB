def send_password(password: str) -> str:
    """
    Used to send connection password.

    This is not the same as what would be used to identify yourself with nickserv, etc.

    :param password:
    :return:
    """
    return f"PASS {password}"


def set_nickname(nickname: str) -> str:
    return f"NICK {nickname}"


def disconnect(reason: str = None) -> str:
    return f"QUIT {reason}" if reason is not None else "QUIT"


def set_mode(target: str, mode: str, enable: bool, params: str = None) -> str:
    flag = "+" if enable else "-"

    return f"MODE {target} {flag}{mode} {params}" if params is not None else f"MODE {target} {flag}{mode}"


def user_invisible(nickname: str, enable: bool = True) -> str:
    return set_mode(nickname, "i", enable)


def user_recieve_wallops(nickname: str, enable: bool = True) -> str:
    return set_mode(nickname, "W", enable)


def user_is_bot(nickname: str, enable: bool = True) -> str:
    return set_mode(nickname, "B", enable)


def user_recieve_server_notices(nickname: str, enable: bool = True) -> str:
    return set_mode(nickname, "s", enable)


def channel_moderated(channel: str, enable: bool = True) -> str:
    return set_mode(channel, "m", enable)


def channel_invite_only(channel: str, enable: bool = True) -> str:
    return set_mode(channel, "i", enable)


def channel_add_autoinvite(channel: str, hostmask: str) -> str:
    return set_mode(channel, "I", True, hostmask)


def channel_remove_autoinvite(channel: str, hostmask: str) -> str:
    return set_mode(channel, "I", False, hostmask)


def channel_set_owner(channel: str, nickname: str, owner: bool = True) -> str:
    return set_mode(channel, "q", owner, nickname)


def channel_set_admin(channel: str, nickname: str, admin: bool = True) -> str:
    return set_mode(channel, "a", admin, nickname)


def channel_set_op(channel: str, nickname: str, op: bool = True) -> str:
    return set_mode(channel, "o", op, nickname)


def channel_set_half_op(channel: str, nickname: str, half_op: bool = True) -> str:
    return set_mode(channel, "h", half_op, nickname)


def channel_set_voice(channel: str, nickname: str, voice: bool = True) -> str:
    return set_mode(channel, "v", voice, nickname)


def channel_list_bans(channel: str) -> str:
    return set_mode(channel, "b", True)


def channel_add_ban(channel: str, hostmask: str) -> str:
    return set_mode(channel, "b", True, hostmask)


def channel_remove_ban(channel: str, hostmask: str) -> str:
    return set_mode(channel, "b", False, hostmask)


def channel_list_ban_exceptions(channel: str) -> str:
    return set_mode(channel, "e", True)


def channel_add_ban_exception(channel: str, hostmask: str) -> str:
    return set_mode(channel, "e", True, hostmask)


def channel_remove_ban_exception(channel: str, hostmask: str) -> str:
    return set_mode(channel, "e", False, hostmask)


def channel_set_limit(channel: str, limit: int = None) -> str:
    if limit is None or limit == 0:
        return set_mode(channel, "l", False)

    return set_mode(channel, "l", True, str(limit))


def channel_set_password(channel: str, password: str = None) -> str:
    if password is None:
        return set_mode(channel, "k", False)

    return set_mode(channel, "k", True, password)


def channel_secret(channel: str, secret: bool = True) -> str:
    return set_mode(channel, "s", secret)


def channel_get_topic(channel: str) -> str:
    return f"TOPIC {channel}"


def channel_set_topic(channel: str, topic: str) -> str:
    return f"TOPIC {channel} :{topic}"


def channel_invite_user(channel: str, nickname: str) -> str:
    return f"INVITE {nickname} {channel}"


def channel_kick_user(channel: str, nickname: str) -> str:
    return f"KICK {channel} {nickname}"


def channel_join(channel: str) -> str:
    return f"JOIN {channel}"


def channel_leave(channel: str, reason: str = None) -> str:
    if reason is None:
        return f"PART {channel}"

    return f"PART {channel} :{reason}"


def say(target: str, message: str) -> str:
    return f"PRIVMSG {target} :{message}"


def ctcp(target: str, message: str) -> str:
    return say(target, chr(1) + message + chr(1))


def emote(target: str, message: str) -> str:
    return ctcp(target, f"ACTION {message}")


def notice(target: str, message: str) -> str:
    return "NOTICE {target} :{message}"


def ctcp_reply(target: str, message: str) -> str:
    return notice(target, chr(1) + message + chr(1))


def send_ping(message: str) -> str:
    return f"PING :{message}"


def send_pong(message: str) -> str:
    return f"PONG :{message}"


def set_user_away(target: str, reason: str) -> str:
    return "AWAY" if reason is None else f"AWAY :{reason}"
