# 2026 MCP Learning from Books

## 日本語

### 概要

このリポジトリは、MCP（Model Context Protocol）を学習するためのサンプルプロジェクト集です。

現在は、FastMCP を使った以下のサンプルを含んでいます。

- 電卓 MCP サーバ
- SQLite テーブル一覧表示 MCP サーバ
- uv を使った Python プロジェクト構成

学習を進めながら、今後ほかの MCP サンプルプロジェクトもフォルダごとに追加していく予定です。

---

### ディレクトリ構成

```text
2026_MCP_learning_from_books/
└── s_書籍_MCP入門/
    └── 01/
        └── mcp-step-03/
            ├── calculator_server.py
            ├── db_server_01.py
            ├── main.py
            ├── pyproject.toml
            ├── uv.lock
            └── README.md
```

---

### プロジェクト内容

#### 1. 電卓 MCP サーバ

`calculator_server.py` は、FastMCP を使った電卓用 MCP サーバです。

利用できる主なツールは以下です。

- `add`：足し算
- `subtract`：引き算
- `multiply`：掛け算
- `divide`：割り算
- `power`：べき乗
- `square_root`：平方根
- `circle_area`：円の面積

---

#### 2. SQLite テーブル一覧表示 MCP サーバ

`db_server_01.py` は、SQLite データベース内のテーブル一覧を取得する MCP サーバです。

`intelligent_shop.db` に接続し、SQLite の `sqlite_master` からユーザーテーブルの一覧と作成 SQL を取得します。

利用できるツールは以下です。

- `list_tables`：DB 内のテーブル一覧を取得

---

#### 3. uv プロジェクト

このプロジェクトは Python のパッケージ管理に `uv` を使用しています。

`pyproject.toml` では、Python 3.12 以上と `fastmcp` を依存関係として指定しています。

---

### 必要環境

- Python 3.12 以上
- uv
- FastMCP

---

### セットアップ

対象フォルダへ移動します。

```bash
cd s_書籍_MCP入門/01/mcp-step-03
```

依存関係をインストールします。

```bash
uv sync
```

---

### 実行方法

#### 電卓 MCP サーバを起動

```bash
uv run python calculator_server.py
```

#### SQLite テーブル一覧表示 MCP サーバを起動

```bash
uv run python db_server_01.py
```

#### main.py を実行

```bash
uv run python main.py
```

---

### Git 管理について

このリポジトリでは、以下は Git 管理対象にします。

- Python ソースコード
- `pyproject.toml`
- `uv.lock`
- `README.md`

以下は Git 管理対象から除外します。

- `.venv/`
- `__pycache__/`
- `.DS_Store`
- `.env`
- ログファイル
- 一時ファイル

`uv.lock` は、同じ依存関係を再現しやすくするため、基本的にコミット対象にしています。

---

### 学習メモ

このリポジトリは、MCP の基本構造を小さく確認するための学習用リポジトリです。

最初は小さな MCP サーバから始め、以下のような流れで拡張していく予定です。

1. シンプルな計算ツールを MCP サーバ化する
2. SQLite などのローカル DB を MCP サーバから参照する
3. ローカル LLM やチャットクライアントと連携する
4. 実務向けのログ解析、DB検索、異常検知などへ発展させる

---

## English

### Overview

This repository contains sample projects for learning MCP（Model Context Protocol）.

The current examples include:

- Calculator MCP server
- SQLite table-list MCP server
- Python project setup using uv

More MCP sample projects will be added in separate folders as learning progresses.

---

### Directory Structure

```text
2026_MCP_learning_from_books/
└── s_書籍_MCP入門/
    └── 01/
        └── mcp-step-03/
            ├── calculator_server.py
            ├── db_server_01.py
            ├── main.py
            ├── pyproject.toml
            ├── uv.lock
            └── README.md
```

---

### Project Contents

#### 1. Calculator MCP Server

`calculator_server.py` is a calculator MCP server built with FastMCP.

Available tools include:

- `add`: addition
- `subtract`: subtraction
- `multiply`: multiplication
- `divide`: division
- `power`: exponentiation
- `square_root`: square root
- `circle_area`: circle area

---

#### 2. SQLite Table List MCP Server

`db_server_01.py` is an MCP server that lists tables from a SQLite database.

It connects to `intelligent_shop.db` and retrieves user-defined tables and their creation SQL from SQLite's `sqlite_master`.

Available tool:

- `list_tables`: list all user-defined tables in the database

---

#### 3. uv Project

This project uses `uv` for Python package and environment management.

The `pyproject.toml` file specifies Python 3.12 or later and depends on `fastmcp`.

---

### Requirements

- Python 3.12 or later
- uv
- FastMCP

---

### Setup

Move to the project directory.

```bash
cd s_書籍_MCP入門/01/mcp-step-03
```

Install dependencies.

```bash
uv sync
```

---

### How to Run

#### Start the calculator MCP server

```bash
uv run python calculator_server.py
```

#### Start the SQLite table-list MCP server

```bash
uv run python db_server_01.py
```

#### Run main.py

```bash
uv run python main.py
```

---

### Git Management

The following files should be committed:

- Python source files
- `pyproject.toml`
- `uv.lock`
- `README.md`

The following files should not be committed:

- `.venv/`
- `__pycache__/`
- `.DS_Store`
- `.env`
- log files
- temporary files

`uv.lock` is intentionally committed so that the same dependency versions can be reproduced on another machine.

---

### Learning Notes

This repository is intended for learning the basic structure of MCP through small examples.

Planned learning steps:

1. Build a simple calculator tool as an MCP server
2. Connect an MCP server to a local SQLite database
3. Integrate with a local LLM or chat client
4. Expand toward practical use cases such as log analysis, database search, and anomaly detection
