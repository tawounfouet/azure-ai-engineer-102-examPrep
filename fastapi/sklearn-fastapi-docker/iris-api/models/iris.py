# from pydantic import BaseModel, conlist
# from typing import List


# class Iris(BaseModel):
#     data: List[conlist(float, min_items=4, max_items=4)]

from pydantic import BaseModel, conlist
from typing import List

class Iris(BaseModel):
    data: List[List[float]]  # Corrected type for data field

    @classmethod
    def from_rows(cls, rows: List[List[float]]):
        """
        Alternative constructor to create Iris objects from data rows.

        Args:
            rows (List[List[float]]): A list of data rows, where each row
                                       represents a flower measurement (4 floats).

        Returns:
            List[Iris]: A list of Iris objects created from the provided rows.
        """

        if not all(len(row) == 4 for row in rows):
            raise ValueError("Each row in 'rows' must have exactly 4 elements (floats).")

        return [cls(data=row) for row in rows]
