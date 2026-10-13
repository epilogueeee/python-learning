class TrafficAnalyzer:
    """交通数据分析器"""

    def __init__(self, source: RecordSource, limit: float = 60):
        self.source = source                  # 组合，不是继承
        self.limit = limit
        self.dataset = TrafficDataset(source.load(), source.errors())   # 只加载一次

    def report(self) -> dict:
        """返回完整统计结果"""

    def overspeed_dataset(self) -> "TrafficDataset":
        """返回超速记录组成的数据集"""