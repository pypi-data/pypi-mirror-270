#!/usr/bin/env python3


class Config:
    """Configuration class"""

    encoding: str = "utf-8"
    chunk: bool = False
    chunk_size: int = 1024
    memory_threshold: int = 25
    filesize_threshold: int = 100
    top_words: int = 20


config = Config()
