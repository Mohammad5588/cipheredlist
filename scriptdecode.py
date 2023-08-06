import re


def decode_script(script):
    # Filter alphanumeric characters from each column and join them
    decoded_columns = [''.join(re.findall(r'[A-Za-z0-9]', column)) for column in script]

    # Join the decoded columns with spaces
    decoded_script = ' '.join(decoded_columns)

    return decoded_script


# Example usage:
script = [
    "(&&&HI(*&&",
    "%$^git*&&^hub*&^#$",
    "^^%%5^^588",
]
decoded_message = decode_script(script)
print(decoded_message)
