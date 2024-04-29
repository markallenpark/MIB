"""
InspIRCd Chanserv Module
"""

from mib.irc import api

def chanserv_command(command: str) -> str:
    """
    This is here to make it less likely for me to mistype the name of the service
    """

    return api.say('chanserv', command)

def ban(channel: str, target: str, reason: str) -> str:
    """
    Ban a user from a channel using either a nickname or a usermask
    """

    return chanserv_command(f'ban {channel} {target} {reason}')

def drop(channel: str) -> str:
    """
    Drop channel registration
    """

    return chanserv_command(f'drop {channel}')

def get_key(channel: str) -> str:
    """
    Get the key of a given channel ( must have access to the channel )
    """

    return chanserv_command(f'getkey {channel}')

def info(channel: str) -> str:
    """
    Get channel info
    """

    return chanserv_command(f'info {channel}')

def invite(channel: str, nick: str|None = None) ->str:
    """
    Tells ChanServ to invite you or an optionally specified
    nick into the given channel.
    """

    if nick is None:
        return chanserv_command(f'invite {channel}')

    return chanserv_command(f'invite {channel} {nick}')

def kick(channel: str, nick: str, reason: str) -> str:
    """
    Kick user from channel
    """

    return chanserv_command(f'kick {channel} {nick} {reason}')

def list_channels(pattern: str) -> str:
    """
    Lists all registered channels matching the given pattern.

    Note that a preceding '#' specifies a range, channel names
    are to be written without '#'.

    Regex matches are also supported using the regex/pcre engine.
    Enclose your pattern in // if this is desired.
    """

    return chanserv_command(f'list {pattern}')

def register(channel: str, description: str|None) -> str:
    """
    Registers a channel in the ChanServ database.  In order
    to use this command, you must first be a channel operator
    on the channel you're trying to register.
    The description, which is optional, is a
    general description of the channel's purpose.
    """

    if description is None:
        return chanserv_command(f'register {channel}')

    return chanserv_command(f'register {channel} {description}')

def status(channel: str, user: str) -> str:
    """
    This command tells you what a users access is on a channel
    and what access entries, if any, they match. Additionally it
    will tell you of any auto kick entries they match. Usage of
    this command is limited to users who have the ability to modify
    access entries on the channel.
    """

    return chanserv_command(f'status {channel} {user}')

def unban(channel: str|None = None, nick: str|None = None) -> str:
    """
    Unban user from channel

    If no channel is specified, you will be unbanned from any and all
    channels where you have permissions to modify the ban list.

    If no nickname is specified, any bans effecting you will be removed
    from the channel, provided you have permissions to modify the ban list
    """
    command = 'unban'

    if channel is not None:
        command += f' {channel}'

        if nick is not None:
            # If unbanning someone else... channel must be specified
            command += ' {nick}'

    return chanserv_command(command)
