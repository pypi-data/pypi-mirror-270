
"""
读取字段配置演示
"""
from excel2db.excel2db import excel2db

if __name__ == "__main__":
    excelUrl = "./demo7.xlsx"
    ed = excel2db("./demo7.json")
    ed.excel2db(excelUrl)
        