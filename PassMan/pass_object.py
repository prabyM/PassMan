"""
This code is meant to help users get the freedom to use complex passwords and forget them without loosing access.
"""


class PassObj:

    def __init__(self, website, user, master):
        self.website = website
        self.user = user


absl = PassObj("absl.com", "admin", "master")






