class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize a Television object with default volume and channel."""
        self.__volume: int = 0  # private volume variable
        self.__channel: int = 0  # private channel variable
        self.__muted: bool = False  # private muted variable
        self.__status: bool = False # private status variable 

    def volume_up(self) -> None:
        """Increase the volume of the television.

        If the volume is at the maximum level, print a message.
        """
        if not self.__status:
            return
        self.__muted  = False
        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume of the television.

        If the volume is at the minimum level, print a message.
        """
        if not self.__status:
            return
        
        self.__muted  = False
        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def channel_up(self) -> None:
        """Switch to the next channel.

        If the current channel is at the maximum, wrap around to the minimum.
        """
        if not self.__status:
            return
        if self.__channel < self.MAX_CHANNEL:
            self.__channel += 1
        else:
            self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """Switch to the previous channel.

        If the current channel is at the minimum, wrap around to the maximum.
        """
        if not self.__status:
            return
        if self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1
        else:
            self.__channel = self.MAX_CHANNEL

    def power(self) -> None:
        """Toggle the power state of the television."""
        self.__status = not self.__status  # toggles power status

    def mute(self) -> None:
        """Toggle the mute state of the television."""
        if not self.__status:
            return
        self.__muted = not self.__muted
    
    def __str__(self) -> str:
        """Return a string representation of the television."""
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"