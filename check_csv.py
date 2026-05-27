import csv

def check_csv_file():
    """
    检查生成的CSV文件内容
    """
    try:
        with open('cq_gov_exam_data.csv', 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            print("CSV文件前10行内容:")
            for i, row in enumerate(reader):
                if i < 10:
                    print(f"第{i+1}行: {row}")
                else:
                    break
        
        print("\nCSV文件已成功创建，总共包含表格数据")
        
    except FileNotFoundError:
        print("CSV文件未找到")
    except Exception as e:
        print(f"读取CSV文件时出现错误: {e}")

if __name__ == "__main__":
    check_csv_file()