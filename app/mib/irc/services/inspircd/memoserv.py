"""
InspIRCd MemoServ Module

MemoServ is a utility allowing IRC users to send short
memos to other IRC users, whether they are online at
the time or not, or to channels(*). Both the sender's
nickname and the target nickname or channel must be
registered in order to send a memo.
"""

from mib.irc import api

def memoserv_command(command: str) -> str:
    """
    Send commands to memoserv
    """

    return api.say('memoserv', command)

def cancel(target: str) -> str:
    """
    Cancels the last memo you sent to the given nick or channel,
    provided it has not been read at the time you use the command.
    """

    return memoserv_command(f'cancel {target}')

def check(nick: str) -> str:
    """
    Checks whether the _last_ memo you sent to nick has been read
    or not. Note that this only works with nicks, not with channels.
    """

    return memoserv_command(f'check {nick}')

def delete(memos: str, channel: str|None):
    """
    Deletes the specified memo or memos. You can supply
    multiple memo numbers or ranges of numbers instead of a
    single number, as in the second example below.

    If LAST is given, the last memo will be deleted.
    If ALL is given, deletes all of your memos.

    memos = '1' deletes the first memo
    memos = '2-5,7-9' deletes memos 2 through 5 and 7 through 9
    memos = 'last' deletes the last memo
    memos = 'all' deletes all memos

    If a channel is specified, it will delete memos for a given channel
    provided you have permissions.
    """

    if channel is None:
        return memoserv_command(f'del {memos}')

    return memoserv_command(f'del {channel} {memos}')

def ignore_list(channel: str|None = None) -> str:
    """
    List of user nicks and masks to ignore. If channel is set,
    list for the given channel, otherwise list for yourself
    """

    if channel is None:
        return memoserv_command(f'ignore {channel} list')

    return memoserv_command('ignore list')

def ignore_add(user: str, channel: str|None = None) -> str:
    """
    Add user by nick or mask to a channel or to your ignore list.

    If channel is provided, channel list will be modified,
    otherwise your list will be modified.
    """

    if channel is None:
        return memoserv_command(f'ignore add {user}')

    return memoserv_command(f'ignore {channel} add {user}')

def ignore_remove(user: str, channel: str|None = None) -> str:
    """
    Remove user by nick or mask from a channel or from your ignore list.

    If channel is provided, channel list will be modified,
    otherwise your list will be modified.
    """

    if channel is None:
        return memoserv_command(f'ignore del {user}')

    return memoserv_command(f'ignore {channel} del {user}')

def info(channel: str|None) -> str:
    """
    Display information on how many memo's or the specified channel has.
    """

    if channel is None:
        return memoserv_command('info')

    return memoserv_command(f'info {channel}')

def read(memos: str, channel: str|None):
    """
    Displays the specified memo or memos. You can supply
    multiple memo numbers or ranges of numbers instead of a
    single number, as in the second example below.

    If LAST is given, the last memo will be deleted.
    If ALL is given, displays all of your memos.

    memos = '1' displays the first memo
    memos = '2-5,7-9' displays memos 2 through 5 and 7 through 9
    memos = 'last' displays the last memo
    memos = 'all' displays all memos

    If a channel is specified, it will delete memos for a given channel
    provided you have permissions.
    """

    if channel is None:
        return memoserv_command(f'read {memos}')

    return memoserv_command(f'read {channel} {memos}')

def send(target: str, memo: str) -> str:
    """
    Sends the named nick or channel a memo containing
    memo-text. When sending to a nickname, the recipient will
    receive a notice that he/she has a new memo. The target
    nickname/channel must be registered.
    """

    return memoserv_command(f'send {target} {memo}')

def notify(mode: str) -> str:
    """
    Changes when you will be notified about new memos:

        ON      You will be notified of memos when you log on,
                   when you unset /AWAY, and when they are sent
                   to you.
        LOGON   You will only be notified of memos when you log
                   on or when you unset /AWAY.
        NEW     You will only be notified of memos when they
                   are sent to you.
        MAIL    You will be notified of memos by email as well as
                   any other settings you have.
        NOMAIL  You will not be notified of memos by email.
        OFF     You will not receive any notification of memos.

    ON is essentially LOGON and NEW combined.
    """

    return memoserv_command(f'set notify {mode}')

def set_limit(limit: int, channel: str|None = None) -> str:
    """
    Sets the maximum number of memos a user or channel is
    allowed to have.  Setting the limit to 0 prevents the user
    from receiving any memos.  If you do not give a channel name,
    your own limit is set.

    Users may only enter a limit for themselves or a channel
    on which they have such privileges, may not remove their
    limit, and may not set a limit above 20.
    """

    if channel is None:
        return memoserv_command(f'set limit {limit}')

    return memoserv_command(f'limit {channel} {limit}')
