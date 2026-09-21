from traffic_io import read_records, write_summary, write_overspeed
from traffic_stats import lane_statistics, count_by_type, average_speed_by_type
from traffic_report import print_errors, print_lane_table, print_type_table
import argparse
import os

def main():

    parser = argparse.ArgumentParser(description="traffic data analyzing tool")
    parser.add_argument("input", help="raw data path")
    parser.add_argument("--limit", type=float, default=60, help="speed limit")
    parser.add_argument("output", help="output path")
    args = parser.parse_args()
    input_path = args.input
    speed_limit = args.limit
    os.makedirs(args.output, exist_ok=True)

    # 1. 读取
    records, errors = read_records(input_path)
    print_errors(errors)
    print(f"成功读取 {len(records)} 条\n")

    if not records:
        print("没有有效数据，程序结束")
        return

    # 2. 统计
    stats = lane_statistics(records)
    counts = count_by_type(records)
    averages = average_speed_by_type(records)

    # 3. 显示
    print_lane_table(stats)
    print()
    print_type_table(counts, averages)

    # 4. 输出文件
    write_summary(stats, "lane_summary.csv")
    write_overspeed(records, speed_limit, "overspeed.csv")
    print("\n结果已写入 lane_summary.csv 和 overspeed.csv")


if __name__ == "__main__":
    main()