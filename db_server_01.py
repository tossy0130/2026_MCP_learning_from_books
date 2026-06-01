#!/usr/bin/env python3

"""

DB Sqlite テーブル一覧表示

"""

import sqlite3
from typing import List, Dict, Any
from fastmcp import FastMCP

# MCP サーバ 作成
mcp = FastMCP("Database Sever - show All")

# DBパス
DB_PATH = 'intelligent_shop.db'

def get_db_connection():
    """ データベース 接続 """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON") # 外部キー制約を有効化
    conn.row_factory = sqlite3.Row # 列名でアクセス可能
    return conn


# *********
# === MCP テーブル一覧を表示
# *********
@mcp.tool()
def list_tables() -> List[Dict[str, Any]]:
    """
    DB内の全てのテーブルを一覧表示

    Returns:
        テーブル名と、説明リスト
    """

    print("[検索]DB テーブル一覧取得中")

    conn = get_db_connection()

    # Sqlite ユーザテーブル取得
    cursor = conn.execute('''
    SELECT name, sql
    FROM sqlite_master
    WHERE type='table' AND name NOT LIKE 'sqlite_%'
    order by name 
    ''')

    tables = []

    for row in cursor.fetchall():
        tables.append({
            "table_name": row["name"],
            "creation_sql": row["sql"]
        })

    conn.close()

    print(f"[完了] {len(tables)} テーブルを取得")
    return tables

if __name__ == "__main__" :
    print("[起動] MCPサーバー(テーブル一覧表示) 起動")
    print("[ツール] 利用可能ルール： list_tables ")
    
    mcp.run()
