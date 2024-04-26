
class Glyph:
    def __init__(
            self,
            name: str,
            advance_width: int = 0,
            advance_height: int = 0,
            horizontal_origin: tuple[int, int] = (0, 0),
            vertical_origin_y: int = 0,
            data: list[list[int]] = None,
    ):
        self.name = name
        self.advance_width = advance_width
        self.advance_height = advance_height
        self.horizontal_origin_x, self.horizontal_origin_y = horizontal_origin
        self.vertical_origin_y = vertical_origin_y
        if data is None:
            data = []
        self.data = data

    @property
    def horizontal_origin(self) -> tuple[int, int]:
        return self.horizontal_origin_x, self.horizontal_origin_y

    @horizontal_origin.setter
    def horizontal_origin(self, value: tuple[int, int]):
        self.horizontal_origin_x, self.horizontal_origin_y = value

    @property
    def width(self) -> int:
        if len(self.data) > 0:
            return len(self.data[0])
        else:
            return 0

    @property
    def height(self) -> int:
        return len(self.data)

    @property
    def dimensions(self) -> tuple[int, int]:
        return self.width, self.height
