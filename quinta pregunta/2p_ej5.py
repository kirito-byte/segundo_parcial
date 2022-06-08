import difflib

diff = difflib.ndiff('Maria\nMarcos\nJuan\n'.splitlines(keepends=True),
             'Moria\nMArcas\nJuan\n'.splitlines(keepends=True))
print(''.join(diff), end="")