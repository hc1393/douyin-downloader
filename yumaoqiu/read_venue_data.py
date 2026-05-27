import csv

def read_venue_data_from_csv(filename='体育馆场地信息.csv'):
    """
    从CSV文件中读取场馆信息，提取ID、库存ID、场馆名称和时间
    """
    venues = []
    
    try:
        with open(filename, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                venue_info = {
                    'id': row['ID'],
                    'stock_id': row['库存ID'],
                    'venue_name': row['场次'],
                    'time_slot': row['时间'],
                    'date': row['日期'],
                    'status': row['状态']
                }
                venues.append(venue_info)
                
        print(f"成功从 {filename} 读取了 {len(venues)} 条场馆信息")
        return venues
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {filename}")
        return []
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return []

def display_selected_venue_info(venues):
    """
    显示提取的场馆信息：ID、库存ID、场馆名称和时间
    """
    if not venues:
        print("没有场馆信息可显示")
        return
        
    print(f"{'ID':<10} {'库存ID':<10} {'场次':<15} {'时间':<15} {'日期':<12} {'状态':<10}")
    print("-" * 75)
    
    for venue in venues:
        print(f"{venue['id']:<10} {venue['stock_id']:<10} {venue['venue_name']:<15} {venue['time_slot']:<15} {venue['date']:<12} {venue['status']:<10}")

if __name__ == "__main__":
    # 读取场馆信息
    venues = read_venue_data_from_csv()
    
    # 显示提取的信息
    display_selected_venue_info(venues)