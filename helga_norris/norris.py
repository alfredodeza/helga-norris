import pkg_resources
import random

from helga.plugins import command


_quips = [quip.rstrip().decode('utf-8') for quip in
          pkg_resources.resource_stream('helga_norris', 'quips.txt')
          if quip.rstrip()]


@command('norris', help="Chuck Norris facts for specific users. Usage: helga norris <nick>")
def norris(client, channel, nick, message, cmd, args):
    global _quips

    try:
        username = (' '.join(args)).strip()
    except:
        username = ''

    if not username:
        return '{0}, I need a nick to use'.format(nick)

    return random.choice(_quips).replace('Chuck Norris', username)
