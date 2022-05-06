import re

def email_parse(email_address):
    match = re.findall(r'([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$', email_address)
    if not match:
        raise ValueError(f'wrong email: {email_address}')
    return dict(zip(['username', 'domain'], match[0]))

print(email_parse('someone@geekbrains.ru'))
