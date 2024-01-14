# TODO Написать 3 класса с документацией и аннотацией типов

from __future__ import annotations
from typing import Union


class BookContainer:
    """
    Abstract class representing a container for books.

    Attributes:
    - capacity: The maximum capacity of the container.
    - current_books: The current number of books in the container.
    """

    def __init__(self, capacity: int):
        """
        Initializes a BookContainer object.

        Args:
        - capacity (int): The maximum capacity of the container.

        Example:
        >>> container = BookContainer(100)
        """
        if not isinstance(capacity, int):
            raise TypeError("Capacity must be of type int")
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.current_books = 0

    def add_book(self) -> None:
        """
        Adds a book to the container.

        Raises:
        - ValueError: If the container is already full.

        Example:
        >>> container = BookContainer(100)
        >>> container.add_book()
        """
        ...

    def remove_book(self) -> None:
        """
        Removes a book from the container.

        Raises:
        - ValueError: If the container is empty.

        Example:
        >>> container = BookContainer(100)
        >>> container.remove_book()
        """
        ...


class NotebookContainer:
    """
    Abstract class representing a container for notebooks.

    Attributes:
    - capacity: The maximum capacity of the container.
    - current_notebooks: The current number of notebooks in the container.
    - has_pocket: Whether the container has a pocket.
    """

    def __init__(self, capacity: int, has_pocket: bool):
        """
        Initializes a NotebookContainer object.

        Args:
        - capacity (int): The maximum capacity of the container.
        - has_pocket (bool): Indicates whether the container has a pocket.

        Example:
        >>> container = NotebookContainer(50, True)
        """
        ...

    def add_notebook(self) -> None:
        """
        Adds a notebook to the container.

        Raises:
        - ValueError: If the container is already full.

        Example:
        >>> container = NotebookContainer(50, True)
        >>> container.add_notebook()
        """
        ...

    def remove_notebook(self) -> None:
        """
        Removes a notebook from the container.

        Raises:
        - ValueError: If the container is empty.

        Example:
        >>> container = NotebookContainer(50, True)
        >>> container.remove_notebook()
        """
        ...


class AlbumContainer:
    """
    Abstract class representing a container for albums.

    Attributes:
    - capacity: The maximum capacity of the container.
    - current_albums: The current number of albums in the container.
    - album_size: The size of each album in the container.
    """

    def __init__(self, capacity: int, album_size: Union[int, float]):
        """
        Initializes an AlbumContainer object.

        Args:
        - capacity (int): The maximum capacity of the container.
        - album_size (Union[int, float]): The size of each album.

        Example:
        >>> container = AlbumContainer(20, 10.5)
        """
        ...

    def add_album(self) -> None:
        """
        Adds an album to the container.

        Raises:
        - ValueError: If the container is already full.

        Example:
        >>> container = AlbumContainer(20, 10.5)
        >>> container.add_album()
        """
        ...

    def remove_album(self) -> None:
        """
        Removes an album from the container.

        Raises:
        - ValueError: If the container is empty.

        Example:
        >>> container = AlbumContainer(20, 10.5)
        >>> container.remove_album()
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass



