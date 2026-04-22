#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import html
from pathlib import Path

# version 1.0 可用

class SearchController:
    def __init__(self, base_path):
        self.data_base_path = Path(base_path)
    
    def search(self, keyword: str) -> str:
        """主搜索方法，返回HTML结果"""
        if not keyword:
            return ""
        
        results = []
        escaped_keyword = re.escape(keyword)
        reg_exp = re.compile(f"({escaped_keyword})", re.IGNORECASE)
        
        # 加载顶部菜单
        with open(self.data_base_path / "topMenu.json", 'r', encoding='utf-8') as f:
            top_menu = json.load(f)
            print(top_menu)
        
        for category, _ in top_menu:
            # 加载分类菜单
            with open(self.data_base_path / f"{category}.json", 'r', encoding='utf-8') as f:
                category_menu = json.load(f)
            
            for section_idx, section in enumerate(category_menu):
                for article_idx, article in enumerate(section["data"]):
                    title, filename, ext = article[0], article[1], article[2]
                    
                    # 构建文件路径
                    file_path = self.data_base_path / category / f"{filename}.{ext}"
                    
                    if file_path.exists():
                        # 搜索文件
                        matches = self._search_file(file_path, reg_exp)
                        
                        if matches:
                            url = f"/index/{category}/{section_idx}_{article_idx}.html"
                            results.append({
                                "title": title,
                                "url": url,
                                "filename": f"{category}/{filename}.{ext}",
                                "matches": matches
                            })
        
        return self._format_results(keyword, results)
    
    def _search_file(self, file_path: Path, reg_exp) -> list:
        """搜索单个文件，返回匹配的行列表"""
        matches = []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    if reg_exp.search(line):
                        # 先转义整行（让 HTML 标签原样显示）
                        safe_line = html.escape(line.rstrip())
                        # 再高亮关键词（在转义后的文本中替换）
                        highlighted = reg_exp.sub(r'<span style="color:red">\1</span>', safe_line)
                        matches.append((line_num, highlighted))
        except Exception:
            pass
        return matches
    
    def _format_results(self, keyword: str, results: list) -> str:
        """格式化搜索结果"""
        if not results:
            return f"<h2>搜索: {html.escape(keyword)}</h2><p>未找到结果</p>"
        
        html_output = f"<h2>搜索: {html.escape(keyword)} (找到 {len(results)} 个文件)</h2>"
        
        for r in results:
            html_output += f"<h3 class='itemHeader'><a href='{r['url']}' target='_blank'>{r['title']}</a> ({r['filename']})</h3>"
            filename=r['filename']
            html_output += "<div class='box'><pre>"
            #for line_num, line in r['matches'][:10]:  # 每个文件最多显示10行
            for line_num, line in r['matches']: #不限制显示行数
                html_output += f"<span style='color:#B13E8D99;'>{filename}</span><span style='color:green'>:{line_num}:</span> {line}\n"
            #if len(r['matches']) > 5:
            #    html_output += f"... 还有 {len(r['matches']) - 5} 处匹配\n"
            html_output += "</pre></div>"
        
        return html_output


# 使用方式
# searcher = SearchController("/path/to/your/data")
# result = searcher.search("关键词")