#!/usr/bin/env python3

"""
MCP サーバ 電卓
"""

import math
from fastmcp import FastMCP

# MCP サーバを作成
mcp = FastMCP("tossy MCP 電卓")

@mcp.tool()
def add(a: float, b: float) -> float:
    """ 2つの数を足します """
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """ 二つの数を引き算する """
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """ 掛け算 """
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """ 割り算 """
    return a / b

@mcp.tool()
def power(a: float, b: float) -> float:
    """ aのb 乗 """
    try:
        return a ** b
    except OverflowError:
        raise ValueError("計算結果が大きすぎます")

@mcp.tool()
def square_root(a: float) -> float:
    """ 平方根 """
    if a < 0:
        raise ValueError("入力値が負の数です")
    return math.sqrt(a)

@mcp.tool()
def circle_area(radius: float) -> float:
    """ 円の面積 """
    if radius < 0:
        raise ValueError("入力値が負の数です")
    return math.pi * radius * radius

if __name__ == "__main__":
    mcp.run() 