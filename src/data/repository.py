import shutil
from typing import Union, Optional, Any
from pathlib import Path


class Repository:
    """
    Repository class to store data as a files in a directory

    Attributes:
        path (Path): path to the directory to store data
    """

    def __init__(self, path: Union[str, Path]):
        """
        Repository class to store data

        Args:
            path (Union[str, Path]): path to the directory to store data
        """

        self.path = Path(path).absolute()
        self.path.mkdir(parents=True, exist_ok=True)

    def __contains__(self, key: str):
        """
        Check if the key is in the repository

        Args:
            key (str): key to check

        Returns:
            bool: True if the key is in the repository, False otherwise
        """

        return (self.path / key).is_file()

    def __getitem__(self, key: str):
        """
        Get content file in the repository

        Args:
            key (str): key to get the content

        Returns:
            str: content of the file
        """

        full_path = self.path / key
        if not full_path.is_file():
            raise KeyError(f"File '{key}' could not be found in '{self.path}'")
        with full_path.open("r", encoding="utf-8") as f:
            return f.read()

    def __setitem__(self, key: Union[str, Path], val: str):
        """
        Set content file in the repository

        Args:
            key (Union[str, Path]): key to store the content
            val (str): content to store
        """

        if str(key).startswith("../"):
            raise ValueError(f"File name '{key}' is not allowed")

        full_path = self.path / key
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(val, encoding="utf-8")

    def __delitem__(self, key: Union[str, Path]):
        """
        Delete file in the repository

        Args:
            key (Union[str, Path]): key to delete
        """

        full_path = self.path / key
        if not full_path.exists():
            raise KeyError(f"File '{key}' could not be found in '{self.path}'")

        if full_path.is_file():
            full_path.unlink()
        elif full_path.is_dir():
            shutil.rmtree(full_path)

    def get(self, key: str, default: Optional[Any] = None):
        """
        Get content file in the repository

        Args:
            key (str): key to get the content
            default (Optional[Any], optional): default value if key is not found. Defaults to None.

        Returns:
            Optional[Any]: content of the file or default value if file doesnt exist
        """

        try:
            return self[key]
        except KeyError:
            return default
