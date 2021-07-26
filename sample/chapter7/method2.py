class Player:
    LEVEL_LIMIT = 10

    @classmethod
    def print_limit(cls):
        print(cls.LEVEL_LIMIT)


Player.print_limit()
