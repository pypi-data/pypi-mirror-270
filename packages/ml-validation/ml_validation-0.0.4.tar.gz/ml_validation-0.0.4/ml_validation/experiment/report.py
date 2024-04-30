from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import numpy.typing as npt
import pandas as pd


@dataclass
class Report:
    version: int
    start: float
    end: float
    authors: list[str]

    table: pd.DataFrame
    matrices: dict[str, npt.NDArray[np.int64]]

    def dump(self, path: Path | str) -> None:
        obj = {
            "version": self.version,
            "start": self.start,
            "end": self.end,
            "autors": self.authors,
            "table": self.table.to_dict(),
            "matrices": {name: matrix.tolist() for name, matrix in self.matrices.items()}
        }
        with open(path, "w") as f:
            json.dump(obj, f, indent=4)

    @staticmethod
    def load(path: Path | str) -> Report:
        with open(path, "r") as f:
            obj = json.load(f)
        return Report(
            version=obj["version"],
            start=obj["start"],
            end=obj["end"],
            authors=obj["autors"],
            table=pd.DataFrame(obj["table"]),
            matrices={name: np.array(matrix) for name, matrix in obj["matrices"].items()}
        )
