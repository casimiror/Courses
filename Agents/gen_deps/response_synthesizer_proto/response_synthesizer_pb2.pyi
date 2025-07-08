from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class getFinalAnswerResponse(_message.Message):
    __slots__ = ("Answer",)
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    Answer: str
    def __init__(self, Answer: _Optional[str] = ...) -> None: ...

class FinalEmpty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FinalParams(_message.Message):
    __slots__ = ("rs_k", "rs_top_k", "rs_temperature", "rs_max_new_tokens", "rs_score_threshold", "rs_repetition_penalty")
    RS_K_FIELD_NUMBER: _ClassVar[int]
    RS_TOP_K_FIELD_NUMBER: _ClassVar[int]
    RS_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    RS_MAX_NEW_TOKENS_FIELD_NUMBER: _ClassVar[int]
    RS_SCORE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RS_REPETITION_PENALTY_FIELD_NUMBER: _ClassVar[int]
    rs_k: int
    rs_top_k: int
    rs_temperature: float
    rs_max_new_tokens: int
    rs_score_threshold: float
    rs_repetition_penalty: float
    def __init__(self, rs_k: _Optional[int] = ..., rs_top_k: _Optional[int] = ..., rs_temperature: _Optional[float] = ..., rs_max_new_tokens: _Optional[int] = ..., rs_score_threshold: _Optional[float] = ..., rs_repetition_penalty: _Optional[float] = ...) -> None: ...

class getFinalAnswerRequest(_message.Message):
    __slots__ = ("query", "params", "qaPairs", "Sources")
    class QaPairsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    QAPAIRS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    query: str
    params: FinalParams
    qaPairs: _containers.ScalarMap[str, str]
    Sources: bytes
    def __init__(self, query: _Optional[str] = ..., params: _Optional[_Union[FinalParams, _Mapping]] = ..., qaPairs: _Optional[_Mapping[str, str]] = ..., Sources: _Optional[bytes] = ...) -> None: ...
