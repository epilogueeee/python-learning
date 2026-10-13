class RecordSource:
    """记录来源的统一接口"""

    def load(self) -> list:
        """返回 TrafficRecord 列表"""
        raise NotImplementedError("子类必须实现 load")

    def errors(self) -> list:
        """返回解析错误 [(行号, 错误描述), ...]，默认无错误"""
        return []

    def describe(self) -> str:
        """一句话描述来源"""
        return f"{type(self).__name__}"


class CsvSource(RecordSource):
    def __init__(self, path: str): ...


class MemorySource(RecordSource):
    def __init__(self, records: list): ...

    @classmethod
    def from_rows(cls, rows: list) -> "MemorySource": ...


class MultiSource(RecordSource):
    def __init__(self, sources: list): ...    # 持有一组 RecordSource