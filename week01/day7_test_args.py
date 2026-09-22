import argparse


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="交通检测数据清洗与统计工具")
    parser.add_argument("input", help="输入 CSV 文件路径")
    parser.add_argument("--limit", type=float, default=60,
                        help="限速值 km/h，默认 60")
    parser.add_argument("--output", default="output",
                        help="输出目录，默认 output")
    return parser.parse_args()


args = parse_args()
print(args.input)       # 文件路径
print(args.limit)       # 限速
print(args.output)      # 输出目录