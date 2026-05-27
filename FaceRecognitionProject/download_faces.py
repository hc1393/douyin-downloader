#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人脸图片下载和预处理脚本
从网络下载人脸图片用于训练
"""

import requests
import os
import cv2
import numpy as np
from urllib.parse import urlparse
import time
from core.face_detector import FaceDetector

class FaceImageDownloader:
    """人脸图片下载器"""
    
    def __init__(self, download_dir="downloaded_faces"):
        self.download_dir = download_dir
        self.face_detector = FaceDetector()
        
        # 创建下载目录
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
            
    def download_image(self, url, filename=None):
        """
        下载单张图片
        
        Args:
            url: 图片URL
            filename: 保存文件名
            
        Returns:
            保存路径或None
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            if not filename:
                # 从URL提取文件名
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path)
                if not filename or '.' not in filename:
                    filename = f"image_{int(time.time())}.jpg"
                    
            # 确保文件名有正确的扩展名
            if not any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
                filename += '.jpg'
                
            filepath = os.path.join(self.download_dir, filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            print(f"✅ 下载成功: {filename}")
            return filepath
            
        except Exception as e:
            print(f"❌ 下载失败 {url}: {e}")
            return None
            
    def extract_faces_from_image(self, image_path, person_name, max_faces=5):
        """
        从图片中提取人脸并保存
        
        Args:
            image_path: 原始图片路径
            person_name: 人员姓名
            max_faces: 最多提取的人脸数量
        """
        try:
            # 读取图片
            image = cv2.imread(image_path)
            if image is None:
                print(f"❌ 无法读取图片: {image_path}")
                return []
                
            # 检测人脸
            faces = self.face_detector.detect_faces(image)
            
            if len(faces) == 0:
                print(f"⚠️  图片中未检测到人脸: {image_path}")
                return []
                
            print(f"🔍 检测到 {len(faces)} 个人脸")
            
            # 创建人员目录
            person_dir = os.path.join("face_data", person_name)
            if not os.path.exists(person_dir):
                os.makedirs(person_dir)
                
            extracted_faces = []
            
            # 提取并保存人脸
            for i, (x, y, w, h) in enumerate(faces[:max_faces]):
                face_roi = image[y:y+h, x:x+w]
                
                # 预处理：调整大小和灰度化
                face_processed = self.face_detector.preprocess_face(face_roi)
                
                # 保存处理后的人脸
                face_filename = f"face_{int(time.time())}_{i}.jpg"
                face_path = os.path.join(person_dir, face_filename)
                cv2.imwrite(face_path, face_processed)
                extracted_faces.append(face_path)
                
                print(f"✅ 提取人脸: {face_filename}")
                
            return extracted_faces
            
        except Exception as e:
            print(f"❌ 处理图片失败 {image_path}: {e}")
            return []
            
    def download_and_process_person(self, person_name, image_urls):
        """
        下载并处理一个人的所有图片
        
        Args:
            person_name: 人员姓名
            image_urls: 图片URL列表
        """
        print(f"\n👤 处理人员: {person_name}")
        print("=" * 40)
        
        downloaded_count = 0
        face_count = 0
        
        for i, url in enumerate(image_urls):
            print(f"\n📥 下载第 {i+1}/{len(image_urls)} 张图片...")
            
            # 下载图片
            filepath = self.download_image(url)
            if filepath:
                downloaded_count += 1
                
                # 提取人脸
                faces = self.extract_faces_from_image(filepath, person_name)
                face_count += len(faces)
                
                # 删除原始下载的图片（节省空间）
                try:
                    os.remove(filepath)
                except:
                    pass
                    
                # 添加延时避免请求过快
                time.sleep(1)
                
        print(f"\n📊 {person_name} 处理完成:")
        print(f"   - 下载图片: {downloaded_count} 张")
        print(f"   - 提取人脸: {face_count} 张")
        
    def get_sample_face_urls(self):
        """
        获取示例人脸图片URL（用于测试）
        注意：这些是公开的测试图片URL
        """
        return {
            "测试人员A": [
                "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400",
                "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400",
                "https://images.unsplash.com/photo-1542909168-82c3e7fdca5c?w=400"
            ],
            "测试人员B": [
                "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=400",
                "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400",
                "https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=400"
            ]
        }

def main():
    """主函数"""
    print("人脸图片下载和训练准备工具")
    print("=" * 50)
    
    downloader = FaceImageDownloader()
    
    # 获取示例数据
    sample_data = downloader.get_sample_face_urls()
    
    print("可选的测试人员:")
    for i, name in enumerate(sample_data.keys(), 1):
        print(f"{i}. {name} ({len(sample_data[name])} 张图片)")
    
    print("\n请选择操作:")
    print("1. 下载所有测试人员数据")
    print("2. 下载指定人员数据")
    print("3. 手动输入自定义人员数据")
    print("0. 退出")
    
    choice = input("\n请输入选择 (0-3): ").strip()
    
    if choice == '1':
        # 下载所有测试人员
        for person_name, urls in sample_data.items():
            downloader.download_and_process_person(person_name, urls)
            
    elif choice == '2':
        # 下载指定人员
        try:
            person_index = int(input("请输入人员编号: ")) - 1
            person_names = list(sample_data.keys())
            if 0 <= person_index < len(person_names):
                person_name = person_names[person_index]
                urls = sample_data[person_name]
                downloader.download_and_process_person(person_name, urls)
            else:
                print("无效的人员编号")
        except ValueError:
            print("请输入有效的数字")
            
    elif choice == '3':
        # 手动输入
        person_name = input("请输入人员姓名: ").strip()
        if person_name:
            print("请输入图片URL（每行一个，输入空行结束）:")
            urls = []
            while True:
                url = input().strip()
                if not url:
                    break
                urls.append(url)
            
            if urls:
                downloader.download_and_process_person(person_name, urls)
            else:
                print("未输入任何URL")
    elif choice == '0':
        print("退出程序")
        return
    else:
        print("无效选择")
        return
    
    print("\n🎉 图片下载和处理完成！")
    print("现在可以运行主程序进行模型训练了")
    print("命令: python main.py")

if __name__ == "__main__":
    main()