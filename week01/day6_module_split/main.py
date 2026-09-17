from traffic_io import read_records, write_summary, write_overspeed
from traffic_stats import lane_statistics, count_by_type
from traffic_report import print_errors, print_lane_table, print_type_table
from average_speed_by_type import average_speed_by_type

def main():
    input_path = "traffic_raw.csv"
    speed_limit = 60

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