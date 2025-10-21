#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import urllib.parse
import binascii

def analyze_cookie_value():
    """Analyze the ssxmod_itna3 cookie value"""
    
    cookie_value = "C50qzxuDRD0D2DRhxjxx0xiqYjYeWKG7iFFQDwhOBDCueqi=i73TuUKQDUAmMG7AxGCD8LKGFD7vP=DBwGpoD/fKuKQxleDARzPM9LDDxGWtCDtdD9DW5Gg74YYDUxGjGDzqi8uxqhEKSyE5TDD5887+5DGI1A=v5x2e4RBi4ZAw4Q2eDSp7WDQeDt2mPgAqaKGoKX00AQ0ffjF4L3GxTtQxh9PeDnPmKB6LxQxkIRtlf6RG09IOutnj64D"
    
    print("=== Analyzing ssxmod_itna3 Cookie Value ===\n")
    print(f"Original cookie: {cookie_value}")
    print(f"Length: {len(cookie_value)}")
    print(f"Contains '=': {'=' in cookie_value}")
    print(f"Contains '+': {'+' in cookie_value}")
    print(f"Contains '/': {'/' in cookie_value}")
    
    # Split by '=' to see if it's key-value pairs
    parts = cookie_value.split('=')
    print(f"\nSplit by '=': {len(parts)} parts")
    for i, part in enumerate(parts):
        print(f"Part {i}: {part[:50]}... (length: {len(part)})")
    
    print("\n" + "="*60)
    
    # Try different decoding methods on each part
    for i, part in enumerate(parts):
        print(f"\n--- Analyzing Part {i} ---")
        print(f"Content: {part}")
        
        # Try base64 decode
        try:
            # Add padding if needed
            missing_padding = len(part) % 4
            if missing_padding:
                padded_part = part + '=' * (4 - missing_padding)
            else:
                padded_part = part
                
            decoded = base64.b64decode(padded_part)
            print(f"Base64 decoded: {decoded}")
            
            # Try to decode as UTF-8
            try:
                utf8_decoded = decoded.decode('utf-8')
                print(f"UTF-8 decoded: {utf8_decoded}")
            except:
                print("UTF-8 decode failed")
                
        except Exception as e:
            print(f"Base64 decode failed: {e}")
        
        # Try URL decode
        try:
            url_decoded = urllib.parse.unquote(part)
            if url_decoded != part:
                print(f"URL decoded: {url_decoded}")
        except Exception as e:
            print(f"URL decode failed: {e}")
            
        print("-" * 40)

if __name__ == "__main__":
    analyze_cookie_value()
