import re

pattern = re.compile(r"""
    ^([a-z0-9_\.-]+)    # first part of email
    @                   # single @ sign
    ([0-9a-z\.-]+)      # email provider
    \.                  # single period
    ([a-z\.]{2,6})$     # com, org, net, etc.
""", re.VERBOSE | re.IGNORECASE)

match = pattern.search("thomas123@yahoo.com")
print(match.group())
print(match.groups())
