import time
import random

def analyze_jo_behavior():
    """
    分析JO函数的行为，解释为什么会产生像"mh4hclexvybssssssso"这样的字符串
    """
    print("JO函数行为分析:")
    print("JavaScript代码:")
    print("function JO() {")
    print("    return Date.now().toString(36) + Math.random().toString(36).substring(2)")
    print("}")
    
    print("\n生成过程分解:")
    
    # 1. 时间戳部分
    timestamp = int(time.time() * 1000)
    timestamp_36 = base36encode(timestamp)
    print(f"1. 时间戳: {timestamp}")
    print(f"2. 36进制时间戳: {timestamp_36}")
    
    # 2. 随机数部分
    random_value = random.random()
    print(f"3. 随机数: {random_value}")
    
    # 3. 随机数转36进制
    random_str = convert_float_to_base36(random_value)
    print(f"4. 随机数36进制: {random_str}")
    
    # 5. 去掉前缀
    random_part = random_str[2:] if random_str.startswith("0.") else random_str
    print(f"5. 去掉'0.'前缀: {random_part}")
    
    # 6. 组合结果
    result = timestamp_36 + random_part
    print(f"6. 最终结果: {result}")
    
    return result

def base36encode(number):
    """
    将整数转换为36进制字符串
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number must be a non-negative integer")
    
    if number == 0:
        return "0"
    
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    while number:
        number, i = divmod(number, 36)
        result = alphabet[i] + result
    
    return result

def convert_float_to_base36(value):
    """
    将0-1之间的浮点数转换为36进制字符串表示
    模拟JavaScript的 toString(36) 行为
    """
    if value == 0:
        return "0"
    
    result = "0."
    # 为了模拟JavaScript的行为，我们需要进行转换
    temp = value
    
    for _ in range(12):  # 限制长度
        temp *= 36
        digit = int(temp)
        result += "0123456789abcdefghijklmnopqrstuvwxyz"[digit]
        temp -= digit
        if temp == 0:
            break
    
    return result

def generate_multiple_examples():
    """
    生成多个示例，展示可能的输出格式
    """
    print("\n\n多个示例:")
    for i in range(10):
        # 使用固定种子以便结果可重现
        random.seed(123 + i)
        example = analyze_jo_behavior()
        print(f"示例 {i+1}: {example}")
        print("-" * 50)

def explain_pattern():
    """
    解释为什么会出现像"mh4hclexvybssssssso"这样的模式
    """
    print("\n为什么会出现连续的's'字符:")
    print("1. Math.random()生成的随机小数在转换为36进制时，")
    print("   如果小数部分有很多接近0的值，就会产生很多's'字符")
    print("2. 在36进制中，'s'代表28，当计算结果为28时就会出现")
    print("3. 连续的's'表示随机数的小数部分在多次乘法后仍然保持特定模式")
    print("4. 这是正常的随机数表现，不是错误")

# 如果直接运行此脚本
if __name__ == "__main__":
    # 重置随机种子以获得可重现的结果
    random.seed(123)
    
    # 分析单个示例
    result = analyze_jo_behavior()
    
    # 解释模式
    explain_pattern()
    
    # 生成多个示例（可选，取消注释以运行）
    # generate_multiple_examples()