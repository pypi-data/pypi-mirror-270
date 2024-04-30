import shutil
from enum import Enum
from pathlib import Path

from . import yadisk


class Type(Enum):
    PTB_XL = 1


def _download_ptb_xl(path_dir: Path, exist_ok: bool) -> None:
    path_dir.mkdir(parents=True, exist_ok=True)
    path_zip = path_dir / "ptb_xl.zip"
    if not exist_ok and path_zip.exists():
        print(f"Archive already exists: {path_zip}")
        return
    yadisk.download(path_zip, "Uzm7r0IFlE2cSw")
    shutil.unpack_archive(path_zip, path_dir, format="zip")
    print("PTB-XL is downloaded and unzipped")


def download(database: Type, path_dir: Path | str = Path.cwd(), exist_ok: bool = False) -> None:
    if isinstance(path_dir, str):
        path_dir = Path(path_dir)
    if database != Type.PTB_XL:
        raise ValueError(f"Unsupported database type: {database}")
    else:
        _download_ptb_xl(path_dir, exist_ok)
