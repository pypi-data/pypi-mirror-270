import ast
import time
from pathlib import Path
from typing import Callable

import numpy as np
import numpy.typing as npt
import pandas as pd

from .metrics import get_metrics
from .report import Report


class Experiment:
    XType = npt.NDArray[np.float32]
    YType = npt.NDArray[np.bool_]
    YPredType = npt.NDArray[np.bool_]
    Function = Callable[[XType], YPredType]
    _CLASSES = ["NORM", "MI", "STTC", "CD", "HYP"]

    def __init__(self, authors: list[str], path: Path) -> None:
        self._start = time.time()
        self._authors = authors
        X = np.load(path / "ptb_xl.npy").astype(np.float32) / 1000
        meta = Experiment._load_metadata(path)
        assert len(X) == len(meta)

        self._X_train, self._meta_train, self._X_test, self._meta_test = Experiment._split(X, meta)

        scp_to_class = Experiment._read_scp_to_class(path)
        self._Y_train = Experiment._get_classes_from_meta(self._meta_train, scp_to_class)
        self._Y_test = Experiment._get_classes_from_meta(self._meta_test, scp_to_class)

    def get_data(self) -> tuple[XType, YType]:
        return self._X_train, self._Y_train

    def get_meta(self) -> pd.DataFrame:
        return self._meta_train

    def validate(self, func: Function) -> Report:
        y_pred = func(self._X_test)
        table, matrices = get_metrics(self._Y_test, y_pred, Experiment._CLASSES)
        return Report(
            version=1,
            start=self._start,
            end=time.time(),
            authors=self._authors,
            table=table,
            matrices=matrices
        )

    @staticmethod
    def _read_scp_to_class(path: Path) -> dict[str, int]:
        scp = pd.read_csv(path / "scp_statements.csv", index_col=0)
        scp = scp[scp.diagnostic == 1]

        scp_to_class = {}
        for d, c in zip(scp.index, scp.diagnostic_class):
            scp_to_class[d] = Experiment._CLASSES.index(c)

        return scp_to_class

    @staticmethod
    def _get_classes_from_meta(meta: pd.DataFrame, scp_to_class: dict[str, int]) -> YType:
        Y = np.zeros((len(meta), len(Experiment._CLASSES)), dtype=np.bool_)
        for i, codes in enumerate(meta.scp_codes):
            for code in codes:
                if code in scp_to_class:
                    Y[i, scp_to_class[code]] = True
        return Y

    @staticmethod
    def _load_metadata(path: Path) -> pd.DataFrame:
        meta = pd.read_csv(path / "ptbxl_database.csv", index_col="ecg_id")
        meta.scp_codes = meta.scp_codes.apply(lambda x: ast.literal_eval(x))
        return meta

    @staticmethod
    def _split(X: XType, meta: pd.DataFrame) -> tuple[XType, pd.DataFrame, XType, pd.DataFrame]:
        test_fold = 10
        X_train = X[np.where(meta.strat_fold != test_fold)]
        meta_train = meta[meta.strat_fold != test_fold]
        X_test = X[np.where(meta.strat_fold == test_fold)]
        meta_test = meta[meta.strat_fold == test_fold]
        return X_train, meta_train, X_test, meta_test


def start_experiment(authors: str | list[str], path_dir: Path | str = Path.cwd()) -> Experiment:
    if isinstance(authors, str):
        authors = [authors]
    if isinstance(path_dir, str):
        path_dir = Path(path_dir)
    return Experiment(authors, path_dir)
