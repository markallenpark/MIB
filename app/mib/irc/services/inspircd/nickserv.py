"""
InspIRCd Nickserv Module
"""
from mib.irc import api

def nickserv_command(command: str) -> str:
    """
    This is here to make it less likely for me to mistype the name of the service
    """
    return api.say('nickserv', command)

def access_add(mask: str) -> str:
    """
    Give access to user to use bot's nick

    mask: str   - user mask (i.e. anyone@*.bepeg.com)
    """

    return nickserv_command(f'access add {mask}')

def access_remove(mask: str) -> str:
    """
    remove access from user to use bot's nick

    mask: str   - user mask (i.e. anyone@*.bepeg.com)
    """

    return nickserv_command(f'access del {mask}')

def access_list() -> str:
    """
    List who has access to use this nick
    """

    return nickserv_command('access list')

def ajoin_add(channel: str, key: str|None = None) -> str:
    """
    Add channel to your auto-join list

    channel: str    - Channel to add
    key: str        - Pass key for channel (optional)
    """

    command = f'ajoin add {channel}'

    if key is not None:
        command += f' {key}'

    return nickserv_command(command)

def ajoin_remove(channel: str) -> str:
    """
    Remove channel from your auto-join list

    channel: str    - Channel to remove
    """
    return nickserv_command(f'ajoin del {channel}')

def ajoin_list() -> str:
    """
    List channels in your auto-join list
    """

    return nickserv_command('ajoin list')

def alist() -> str:
    """
    List channels that you have access on
    """

    return nickserv_command('alist')

def cert_add(fingerprint: str|None = None) -> str:
    """
    Add your current or specified fingerprint to cert list so that nickserv
    can automatically identify you.

    fingerprint: str|None   - specify a fingerprint (Optional)
    """
    if fingerprint is not None:
        return nickserv_command(f'cert add {fingerprint}')
    return nickserv_command('cert add')

def cert_revoke(fingerprint: str) -> str:
    """
    Remove a fingerprint from your automatic identification cert list

    fingerprint: str    - Fingerprint to revoke access to
    """

    return nickserv_command(f'cert del {fingerprint}')

def cert_list() -> str:
    """
    List certs that are authorized on your automatic identification cert list
    """

    return nickserv_command('cert list')

def confirm(passcode: str) -> str:
    """
    Confirm registration passcode
    """

    return nickserv_command(f'confirm {passcode}')

def drop(nickname: str) -> str:
    """
    Drop the registration of a nickname
    """

    return nickserv_command(f'drop {nickname}')

def group_add(target_nickname: str, password: str) -> str:
    """
    Add current nickname to nick group

    target_nickname: str    - Nickname already in group
    password: str           - Password for nicknames in group
    """

    return nickserv_command(f'group {target_nickname} {password}')

def group_remove(nickname: str|None = None) -> str:
    """
    This command ungroups your nick, or if given, the specificed nick,
    from the group it is in. The ungrouped nick keeps its registration
    time, password, email, greet, language, and url. Everything else
    is reset. You may not ungroup yourself if there is only one nick in
    your group.

    nickname: str|None  - Nickname to remove from group if not current (optional)
    """

    if nickname is not None:
        return nickserv_command(f'ungroup {nickname}')

    return nickserv_command('ungroup')

def group_list() -> str:
    """
    List all nicknames in your group
    """

    return nickserv_command('glist')

def identify(password: str, nickname: str|None = None) -> str:
    """
    Identify yourself with nickserv

    password: str   - Password for your nickserv account
    nickname: str   - Nickname for if you're not currently using the nickname
                      for which you're identifying ( optional )
    """

    if nickname is not None:
        return nickserv_command(f'identify {nickname} {password}')

    return nickserv_command(f'identify {password}')

def info(nickname: str|None) -> str:
    """
    Displays information about the given nickname, such as
    the nick's owner, last seen address and time, and nick
    options. If no nick is given, and you are identified,
    your account name is used, else your current nickname is
    used.

    nickname: str   - Nickname to get info about (optional)
    """

    if nickname is not None:
        nickserv_command(f'info {nickname}')

    return nickserv_command('info')

def nick_list(mask: str) -> str:
    """
    Lists all registered nicknames which match the given
    pattern, in nick!user@host format.
    """

    return nickserv_command(f'list {mask}')

def logout() -> str:
    """
    Logout of nickserv
    """

    return nickserv_command('logout')


def recover(nickname: str, password: str) -> str:
    """
    Recovers your nick by kicking any services or users currently using it off of it.
    """

    return nickserv_command(f'recover {nickname} {password}')

def register(password: str, email: str) -> str:
    """
    Register current nick with nickserv
    """

    return nickserv_command(f'register {password} {email}')

def resend() -> str:
    """
    This command will resend you the registration confirmation email.
    """

    return nickserv_command('resend')

def reset_password(nickname: str, email: str) -> str:
    """
    Sends a passcode to the nickname with instructions on how to
    reset their password.  Email must be the email address associated
    to the nickname.

    nickname: str   - Nickname to reset password for
    email: str      - Email address ( must match the one associated with nickname )
    """

    return nickserv_command(f'reset {nickname} {email}')

def update() -> str:
    """
    Updates your current status, i.e. it checks for new memos,
    sets needed channel modes and updates your vhost and
    your userflags (lastseentime, etc).
    """

    return nickserv_command('update')

def set_autop(enable: bool) -> str:
    """
    Sets whether you will be given your channel status modes automatically.
    Set to ON to allow ChanServ to set status modes on you automatically
    when entering channels. Note that depending on channel settings some modes
    may not get set automatically.

    enable: bool    - If True, enable autoop, if False, disable autoop
    """
    flag = 'on' if enable else 'off'

    return nickserv_command(f'set autoop {flag}')

def set_display_nick(nickname: str) -> str:
    """
    Changes the display used to refer to your nickname group in
    Services. The new display MUST be a nick of your group.

    nickname: str   - Nickname to set
    """

    return nickserv_command(f'set display {nickname}')

def set_email(email: str) -> str:
    """
    Associates the given E-mail address with your nickname.
    This address will be displayed whenever someone requests
    information on the nickname with the INFO command.

    email: str  - Email to set
    """

    return nickserv_command(f'set email {email}')

def set_greet(message: str) -> str:
    """
    Makes the given message the greet of your nickname, that
    will be displayed when joining a channel that has GREET
    option enabled, provided that you have the necessary
    access on it.

    message: str    - Message to set
    """

    return nickserv_command(f'set greet {message}')

def hide_email(enable: bool) -> str:
    """
    Set/unset Email display on INFO output

    enable: bool    - True to hide, False to show
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set hide email {flag}')

def hide_services_status(enable: bool) -> str:
    """
    Set/unset your services access status on INFO output

    enable: bool    - True to hide, False to show
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set hide status {flag}')

def hide_last_user_mask(enable: bool) -> str:
    """
    Set/unset your last seen usermask

    enable: bool    - True to hide, False to show
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set hide usermask {flag}')

def hide_last_quit(enable: bool) -> str:
    """
    Set/unset your last quit message

    enable: bool    - True to hide, False to show
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set hide quit {flag}')

def keep_modes(enable: bool) -> str:
    """
    Enables or disables keepmodes for your nick. If keep
    modes is enabled, services will remember your usermodes
    and attempt to re-set them the next time you authenticate.
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set keepmodes {flag}')

def set_kill(enable: bool) -> str:
    """
    Turns the automatic protection option for your nick
    on or off. With protection on, if another user
    tries to take your nick, they will be given one minute to
    change to another nick, after which NickServ will forcibly change
    their nick.
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set kill {flag}')

def set_language(language: str) -> str:
    """
    Changes the language Services uses when sending messages to
    you (for example, when responding to a command you send).
    """

    return nickserv_command(f'set language {language}')

def set_message(enable: bool) -> str:
    """
    Allows you to choose the way Services are communicating with
    you. With MESSAGE set, Services will use messages, else they'll
    use notices.
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set message {flag}')

def set_password(password: str) -> str:
    """
    Change your password for identifying with Nickserv
    """

    return nickserv_command(f'set password {password}')

def set_private(enable: bool) -> str:
    """
    Turns NickServ's privacy option on or off for your nick.
    With PRIVATE set, your nickname will not appear in
    nickname lists generated with NickServ's LIST command.
    (However, anyone who knows your nickname can still get
    information on it using the INFO command.)
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set private {flag}')

def set_secure(enable: bool) -> str:
    """
    Turns NickServ's security features on or off for your
    nick. With SECURE set, you must enter your password
    before you will be recognized as the owner of the nick,
    regardless of whether your address is on the access
    list. However, if you are on the access list, NickServ
    will not auto-kill you regardless of the setting of the
    KILL option.
    """

    flag = 'on' if enable else 'off'

    return nickserv_command(f'set secure {flag}')

def set_url(url: str) -> str:
    """
    Associate a URL with your account
    """

    return nickserv_command(f'set url {url}')
