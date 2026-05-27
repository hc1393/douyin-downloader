import csv
import pandas as pd

def analyze_cq_gov_data():
    """
    分析重庆市公务员考试数据
    """
    try:
        # 读取CSV文件
        df = pd.read_csv('cq_gov_exam_data.csv', encoding='utf-8-sig')
        
        print("数据概览:")
        print(f"总行数: {len(df)}")
        print(f"列名: {list(df.columns)}")
        
        print("\n前5行数据:")
        print(df.head())
        
        # 数据类型
        print("\n数据类型:")
        print(df.dtypes)
        
        # 转换数值列为数字类型
        numeric_columns = ['计划招考人数', '报考人数', '审核通过人数', '交费人数']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # 统计信息
        print("\n数值列统计信息:")
        print(df[numeric_columns].describe())
        
        # 热门岗位分析
        if '报考职位' in df.columns and '报考人数' in df.columns:
            print("\n报考人数最多的前10个职位:")
            top_positions = df.nlargest(10, '报考人数')[['报考单位', '报考职位', '报考人数']]
            print(top_positions)
        
        # 主管单位统计
        if '主管单位' in df.columns:
            print("\n各主管单位职位数量统计:")
            dept_counts = df['主管单位'].value_counts()
            print(dept_counts.head(10))
        
        # 保存分析结果
        df.to_csv('cq_gov_exam_data_analyzed.csv', index=False, encoding='utf-8-sig')
        print("\n分析后的数据已保存到 cq_gov_exam_data_analyzed.csv")
        
        return df
        
    except FileNotFoundError:
        print("未找到CSV文件，请先运行cq_gov_final.py脚本")
        return None
    except Exception as e:
        print(f"分析数据时出现错误: {e}")
        return None

def export_summary_statistics():
    """
    导出汇总统计数据
    """
    try:
        df = pd.read_csv('cq_gov_exam_data.csv', encoding='utf-8-sig')
        
        # 转换数值列
        numeric_columns = ['计划招考人数', '报考人数', '审核通过人数', '交费人数']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # 计算汇总统计
        summary_stats = {
            '总职位数': len(df),
            '总招考人数': df['计划招考人数'].sum() if '计划招考人数' in df.columns else 0,
            '总报考人数': df['报考人数'].sum() if '报考人数' in df.columns else 0,
            '平均竞争比': round(df['报考人数'].mean(), 2) if '报考人数' in df.columns else 0,
            '最高报考人数': df['报考人数'].max() if '报考人数' in df.columns else 0,
            '最低报考人数': df['报考人数'].min() if '报考人数' in df.columns else 0
        }
        
        # 保存汇总统计到单独的CSV
        with open('cq_gov_summary_stats.csv', 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['统计项', '数值'])
            for key, value in summary_stats.items():
                writer.writerow([key, value])
        
        print("汇总统计数据已保存到 cq_gov_summary_stats.csv")
        print("\n汇总统计:")
        for key, value in summary_stats.items():
            print(f"{key}: {value}")
        
    except Exception as e:
        print(f"导出汇总统计时出现错误: {e}")

if __name__ == "__main__":
    print("开始分析重庆市公务员考试数据...")
    df = analyze_cq_gov_data()
    
    if df is not None:
        print("\n" + "="*50)
        export_summary_statistics()