"""
Sarmat.
Описание сущностей.
Базовый класс для описания моделей.
"""
from dataclasses import asdict, dataclass, fields
from typing import Any, Dict, List, Optional

from sarmat.core.constants import PeriodType


@dataclass
class BaseModel:

    @property
    def sarmat_fields(self):
        return [fld.name for fld in fields(self)]

    @property
    def as_dict(self):
        return asdict(self)


@dataclass
class BaseIdModel:

    id: Optional[int] = 0


@dataclass
class BaseUidModel:

    uid: Optional[str] = ""


@dataclass
class CustomAttributesModel:

    custom_attributes: Optional[Dict[str, Any]] = None

    @property
    def custom_fields(self) -> List[str]:
        return list(self.custom_attributes.keys()) if self.custom_attributes else []


@dataclass
class PersonModel(BaseModel):
    """Данные человека"""

    last_name: str      # фамилия
    first_name: str     # имя
    middle_name: str    # отчество
    male: bool          # пол: М


@dataclass
class BasePeriodItemModel(BaseModel):
    """Элементы сложного периода"""

    period_type: PeriodType     # тип периода
    cypher: str                 # шифр (константа)
    name: str                   # название
    value: List[int]            # список значений
    is_active: bool             # период активности


@dataclass
class PeriodItemModel(BaseIdModel, CustomAttributesModel, BasePeriodItemModel):
    """Описание модели 'Элемент периода'"""


@dataclass
class BasePeriodModel(BaseModel):
    """Период (перечень значимых атрибутов)"""

    cypher: str                                         # системное имя
    name: str                                           # константа
    periods: Optional[List[PeriodItemModel]] = None     # описание сложного периода
    period: Optional[PeriodItemModel] = None            # описание простого периода


@dataclass
class PeriodModel(BaseIdModel, CustomAttributesModel, BasePeriodModel):
    """Описание модели 'Период'"""
