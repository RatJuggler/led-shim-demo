

class NotAnEffect():
    """
    Not an effect (doesn't inherit from AbstractEffect).
    """

    def __init__(self) -> None:
        pass

    def compose(self) -> None:
        pass

    def __repr__(self) -> str:
        return "NotAnEffect()"
