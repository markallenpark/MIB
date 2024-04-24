""" Generate IRC API Command Strings """

def send_password(password: str) -> str:
    """
    Used to send connection password.

    This is not the same as what would be used to identify yourself with nickserv, etc.
    """
    return f"PASS {password}"


def set_nickname(nickname: str) -> str:
    """ Set nickname """
    return f"NICK {nickname}"


def set_username(username: str, realname: str) -> str:
    """ Set username and realname """
    return f"USER {username} 0 * :{realname}"


def disconnect(reason: str | None = None) -> str:
    """ Disconnect from server """
    return f"QUIT {reason}" if reason is not None else "QUIT"


def set_mode(target: str, mode: str, enable: bool, params: str | None = None) -> str:
    """ Set/unset mode flags """
    flag = "+" if enable else "-"

    if params is not None:
        return f"MODE {target} {flag}{mode} {params}"

    return f"MODE {target} {flag}{mode}"


def user_invisible(nickname: str, enable: bool = True) -> str:
    """ Set/unset user invisible flag """
    return set_mode(nickname, "i", enable)


def user_recieve_wallops(nickname: str, enable: bool = True) -> str:
    """ Set/unset user wallops flag """
    return set_mode(nickname, "W", enable)


def user_is_bot(nickname: str, enable: bool = True) -> str:
    """ Set/unset user bot flag """
    return set_mode(nickname, "B", enable)


def user_recieve_server_notices(nickname: str, enable: bool = True) -> str:
    """ Set/unset user server notices flag """
    return set_mode(nickname, "s", enable)


def channel_moderated(channel: str, enable: bool = True) -> str:
    """ Set/unset channel moderation flag """
    return set_mode(channel, "m", enable)


def channel_invite_only(channel: str, enable: bool = True) -> str:
    """ Set/unset require channel invite flag """
    return set_mode(channel, "i", enable)


def channel_add_autoinvite(channel: str, hostmask: str) -> str:
    """ Add user to channel auto-invite list """
    return set_mode(channel, "I", True, hostmask)


def channel_remove_autoinvite(channel: str, hostmask: str) -> str:
    """ Remove user from channel auto-invite list """
    return set_mode(channel, "I", False, hostmask)


def channel_auto_invite_list(channel: str) -> str:
    """ Request auto-invite list """
    return set_mode(channel, 'I', True)


def channel_set_owner(channel: str, nickname: str, owner: bool = True) -> str:
    """ Set/unset channel owner flag """
    return set_mode(channel, "q", owner, nickname)


def channel_set_admin(channel: str, nickname: str, admin: bool = True) -> str:
    """ Set/unset channel admin flag """
    return set_mode(channel, "a", admin, nickname)


def channel_set_op(channel: str, nickname: str, op: bool = True) -> str:
    """ Set/unset channel operator flag """
    return set_mode(channel, "o", op, nickname)


def channel_set_half_op(channel: str, nickname: str, half_op: bool = True) -> str:
    """ Set/unset channel half-operator flag """
    return set_mode(channel, "h", half_op, nickname)


def channel_set_voice(channel: str, nickname: str, voice: bool = True) -> str:
    """ Set/unset channel voice permission flag """
    return set_mode(channel, "v", voice, nickname)


def channel_list_bans(channel: str) -> str:
    """ Request channel ban list """
    return set_mode(channel, "b", True)


def channel_add_ban(channel: str, hostmask: str) -> str:
    """ Add user to channel ban list """
    return set_mode(channel, "b", True, hostmask)


def channel_remove_ban(channel: str, hostmask: str) -> str:
    """ remove user from channel ban list """
    return set_mode(channel, "b", False, hostmask)


def channel_list_ban_exceptions(channel: str) -> str:
    """ Request channel ban list exceptions """
    return set_mode(channel, "e", True)


def channel_add_ban_exception(channel: str, hostmask: str) -> str:
    """ Add user channel ban exception """
    return set_mode(channel, "e", True, hostmask)


def channel_remove_ban_exception(channel: str, hostmask: str) -> str:
    """ Remove user channel ban exception """
    return set_mode(channel, "e", False, hostmask)


def channel_set_limit(channel: str, limit: int | None = None) -> str:
    """ Set/unset channel user limit """

    if limit is None or limit == 0:
        return set_mode(channel, "l", False)

    return set_mode(channel, "l", True, str(limit))


def channel_set_password(channel: str, password: str | None = None) -> str:
    """ Set/unset channel password """
    if password is None:
        return set_mode(channel, "k", False)

    return set_mode(channel, "k", True, password)


def channel_secret(channel: str, secret: bool = True) -> str:
    """ Set/unset channel is secret/hidden from channel list """
    return set_mode(channel, "s", secret)


def channel_get_topic(channel: str) -> str:
    """ Request channel topic """
    return f"TOPIC {channel}"


def channel_set_topic(channel: str, topic: str) -> str:
    """ Set channel topic """
    return f"TOPIC {channel} :{topic}"


def channel_invite_user(channel: str, nickname: str) -> str:
    """ Invite user to channel """
    return f"INVITE {nickname} {channel}"


def channel_kick_user(channel: str, nickname: str) -> str:
    """ Kick user from channel """
    return f"KICK {channel} {nickname}"


def channel_join(channel: str) -> str:
    """ Join a channel """
    return f"JOIN {channel}"


def channel_leave(channel: str, reason: str | None = None) -> str:
    """ Leave a channel """
    if reason is None:
        return f"PART {channel}"

    return f"PART {channel} :{reason}"


def say(target: str, message: str) -> str:
    """ Send a PRIVMSG to a target """
    return f"PRIVMSG {target} :{message}"


def ctcp(target: str, message: str) -> str:
    """ Set PRIVMSG subtype to CTCP """
    return say(target, chr(1) + message + chr(1))


def emote(target: str, message: str) -> str:
    """ Set PRIVMSG subtype to ACTION """
    return ctcp(target, f"ACTION {message}")


def notice(target: str, message: str) -> str:
    """ Send a notice to a target """
    return f"NOTICE {target} :{message}"


def ctcp_reply(target: str, message: str) -> str:
    """ Set NOTICE subtype to CTCP-reply """
    return notice(target, chr(1) + message + chr(1))


def send_ping(message: str) -> str:
    """ Ping network """
    return f"PING :{message}"


def send_pong(message: str) -> str:
    """ Respond to network ping """
    return f"PONG :{message}"


def set_user_away(reason: str) -> str:
    """ Set/unset user away flag """
    return "AWAY" if reason is None else f"AWAY :{reason}"
