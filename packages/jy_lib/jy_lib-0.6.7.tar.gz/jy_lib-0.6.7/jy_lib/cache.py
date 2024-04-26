# -*- coding: utf-8 -*-
import inspect
import lz4.frame
import math
import os
import pickle
import re
import sqlite3
import time
from typing import Any, Set, List, Tuple, Dict


class Cache:
    """持久化TTL缓存"""

    def __init__(self, path: str = None):
        current_frame = inspect.currentframe()
        caller_frame = current_frame.f_back
        caller_file = caller_frame.f_code.co_filename
        if not path:
            path: str = f'_{os.path.splitext(os.path.basename(caller_file))[0]}.db3'
        self.path: str = os.path.join(os.path.dirname(caller_file), path)
        self.default_dataset: str = 'DEFAULT'
        self.conn = sqlite3.connect(self.path)
        self.conn.execute('PRAGMA auto_vacuum = FULL')
        self.datasets: Set[str] = self.get_tables()

    def get_tables(self) -> Set[str]:
        """获取所有数据集"""
        cursor = self.conn.cursor()
        r = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return {row[0] for row in r.fetchall()}

    def create_table(self, dataset: str) -> None:
        """创建数据集"""
        assert not re.findall(r'\s', dataset)
        self.conn.execute(f"""CREATE TABLE IF NOT EXISTS `{dataset}` (
            `key` TEXT PRIMARY KEY NOT NULL,
            `value` BLOB NOT NULL,
            `expired_at` REAL NOT NULL
        )""")
        self.conn.execute(f"""CREATE INDEX IF NOT EXISTS expired_at ON `{dataset}` (`expired_at`)""")
        self.conn.commit()

    def set(self, dataset: str = None, key: str = '', value: Any = None, expire: float = math.inf) -> None:
        """设置键值"""
        if not dataset:
            dataset = self.default_dataset
        assert isinstance(dataset, str), 'dataset必须是字符串'
        assert dataset, 'dataset不能为空'
        assert isinstance(key, str), 'key必须是字符串'
        assert key, 'key不能为空'
        if dataset not in self.datasets:
            self.create_table(dataset=dataset)
            self.datasets.clear()
            self.datasets.update(self.get_tables())
        payload: bytes = lz4.frame.compress(pickle.dumps(value))
        sql: str = f"""REPLACE INTO `{dataset}` (`key`, `value`, `expired_at`) VALUES(?,?,?)"""
        self.conn.execute(sql, (key, payload, time.time() + expire))
        self.conn.commit()

    def update(self, dataset: str = None, items: Dict[str, Any] = None, expire: float = math.inf) -> None:
        """批量设置键值"""
        if not dataset:
            dataset = self.default_dataset
        assert isinstance(dataset, str), 'dataset必须是字符串'
        assert dataset, 'dataset不能为空'
        assert isinstance(items, dict), 'items必须是字典'
        if not items:
            return
        for key in items.keys():
            assert isinstance(key, str), 'key必须是字符串'
            assert key, 'key不能为空'
        if dataset not in self.datasets:
            self.create_table(dataset=dataset)
            self.datasets.clear()
            self.datasets.update(self.get_tables())
        ps: List[Tuple] = []
        now = time.time()
        for key, value in items.items():
            payload: bytes = lz4.frame.compress(pickle.dumps(value))
            ps.append((key, payload, now + expire))
        sql: str = f"""REPLACE INTO `{dataset}` (`key`, `value`, `expired_at`) VALUES(?,?,?)"""
        self.conn.executemany(sql, ps)
        self.conn.commit()

    def delete(self, dataset: str = None, key: str = '') -> None:
        """删除键值对"""
        if not dataset:
            dataset = self.default_dataset
        assert isinstance(dataset, str), 'dataset必须是字符串'
        assert dataset, 'dataset不能为空'
        assert isinstance(key, str), 'key必须是字符串'
        assert key, 'key不能为空'
        if dataset in self.datasets:
            sql: str = f"""DELETE FROM `{dataset}` WHERE `key`=?"""
            self.conn.execute(sql, (key, ))
            self.conn.commit()

    def get(self, dataset: str = None, key: str = '') -> Any | None:
        """获取键值"""
        if not dataset:
            dataset = self.default_dataset
        assert isinstance(dataset, str), 'dataset必须是字符串'
        assert dataset, 'dataset不能为空'
        assert isinstance(key, str), 'key必须是字符串'
        assert key, 'key不能为空'
        if dataset in self.datasets:
            cursor = self.conn.cursor()
            sql: str = f"""SELECT `value`, `expired_at` FROM `{dataset}` WHERE `key`=?"""
            r = cursor.execute(sql, (key, ))
            r = r.fetchone()
            if r is None:
                return r
            else:
                value, expired_at = r
                if expired_at > time.time():
                    return pickle.loads(lz4.frame.decompress(value))
                else:
                    self.delete(dataset=dataset, key=key)
                    return None

    def keys(self, dataset: str = None) -> List[str] | None:
        """列出所有键名"""
        if not dataset:
            dataset = self.default_dataset
        assert isinstance(dataset, str), 'dataset必须是字符串'
        assert dataset, 'dataset不能为空'
        if dataset in self.datasets:
            cursor = self.conn.cursor()
            sql: str = f"""SELECT `key` FROM `{dataset}` WHERE `expired_at`>?"""
            r = cursor.execute(sql, (time.time(), ))
            return [r[0] for r in r.fetchall()]

    def drop_table(self, dataset: str):
        """删除数据集"""
        assert isinstance(dataset, str), 'dataset必须是字符串'
        assert dataset, 'dataset不能为空'
        if dataset in self.datasets:
            sql: str = f"""DROP TABLE IF EXISTS `{dataset}`"""
            self.conn.execute(sql)
            self.conn.commit()
            self.datasets.discard(dataset)

    def vacuum(self, force: bool = True):
        key_vacuum_at: str = '__VACUUM__'
        vacuum_at: int | None = self.get(key=key_vacuum_at)
        if force or not vacuum_at or time.time() - vacuum_at >= 86400:
            self.conn.execute('VACUUM')
            self.set(key=key_vacuum_at, value=int(time.time()))

    def close(self):
        self.conn.commit()
        self.vacuum(force=False)
        self.conn.close()
