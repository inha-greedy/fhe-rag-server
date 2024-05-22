import base64

from Pyfhel import PyCtxt, Pyfhel
from pydantic import BaseModel, Field


# not use Similarity Model (all data in server are encrypted)


class PyCSimilarity(BaseModel):
    index: int
    score: PyCtxt = Field(default_factory=PyCtxt())

    class Config:
        arbitrary_types_allowed = True


class PyCSimilarityDto(BaseModel):
    index: int
    score: str

    def to_dict(self):
        return {
            "index": self.index,
            "score": self.score,
        }

    def to_similarity(self, he: Pyfhel):
        index = self.index
        score = PyCtxt(pyfhel=he, bytestring=base64.b64decode(self.score))

        return PyCSimilarity(index=index, score=score)
