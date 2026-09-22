from traffic_io import read_records, write_summary, write_overspeed, write_type_summary, write_error_log
from traffic_stats import lane_statistics, count_by_type, average_speed_by_type, flow_by_minute, find_peak_minute
from traffic_report import print_errors, print_lane_table, print_type_table, print_flow_distribution
import argparse
import os

def main():

    parser = argparse.ArgumentParser(description="traffic data analyzing tool")
    parser.add_argument("input", help="raw data path")
    parser.add_argument("--limit", type=float, default=60, help="speed limit")
    parser.add_argument("--output", default="output", help="output path")
    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    lane_summary_path = os.path.join(args.output, "lane_summary.csv")
    overspeed_path = os.path.join(args.output, "overspeed.csv")
    type_summary_path = os.path.join(args.output, "type_summary.csv")
    error_log_path = os.path.join(args.output, "error_log.txt")
    input_path = args.input
    speed_limit = args.limit

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
    flow = flow_by_minute(records)
    max_flow = find_peak_minute(flow)

    # 3. 显示
    print_lane_table(stats)
    print()
    print_type_table(counts, averages)
    print_flow_distribution(flow, max_flow)
    

    # 4. 输出文件
    write_summary(stats, lane_summary_path)
    write_overspeed(records, speed_limit, overspeed_path)
    write_type_summary(counts, averages, type_summary_path)
    write_error_log(errors, input_path, error_log_path)
    print("\n结果已写入")


if __name__ == "__main__":
    main()