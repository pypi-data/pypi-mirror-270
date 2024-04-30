
demo = {
    "demo1":{
        "file":"""
\"\"\"
快速演示
\"\"\"
from excel2db.excel2db import excel2db

if __name__ == "__main__":
    excelUrl = "./demo1.xlsx"
    ed = excel2db()
    ed.excel2db(excelUrl)
        """,
        "json":"",
        "excel":[
            {
                "sheetName":"st1",
                "data":[
                    ["姓名","性别"],
                    ["张三","男"],
                    ["李四","女"]
                ]
            }
        ]
    },
    "demo2":{
        "file":"""
\"\"\"
无标题文件
\"\"\"
from excel2db.excel2db import excel2db

if __name__ == "__main__":
    excelUrl = "./demo2.xlsx"
    ed = excel2db("./demo2.json")
    ed.excel2db(excelUrl)
        """,
        "json":"""
{
  "sheet" : [
    {
      "sheetID" : 0,
      "titleLines" : 0
    }
  ]
}
        """,
        "excel":[
            {
                "sheetName":"st1",
                "data":[
                    ["张三","男"],
                    ["李四","女"]
                ]
            }
        ]
    },
    "demo3":{
        "file":"""
\"\"\"
明细表示例
\"\"\"
from excel2db.excel2db import excel2db

if __name__ == "__main__":
    excelUrl = "./demo3.xlsx"
    ed = excel2db("./demo3.json")
    ed.excel2db(excelUrl)
        """,
        "json":"""
{
  "sheet" : [
    {
      "sheetID" : 0,
      "isIncludeDetail" : true,
      "detailSplitByColumnID" : "C",
      "detailTitle": {
        "detailTitleName":[
          "科目"
        ]
      }
    }
  ]
}
        """,
        "excel":[
            {
                "sheetName":"st1",
                "data":[
                    ["姓名","性别","语文","数学","英语"],
                    ["张三","男",56,67,76],
                    ["李四","女",45,34,54]
                ]
            }
        ]
    },
    "demo4":{
        "file":"""
\"\"\"
多sheet演示
\"\"\"
from excel2db.excel2db import excel2db

if __name__ == "__main__":
    excelUrl = "./demo4.xlsx"
    ed = excel2db()
    ed.excel2db(excelUrl)
        """,
        "json":"""
        """,
        "excel":[
            {
                "sheetName":"st1",
                "data":[
                    ["姓名","性别"],
                    ["张三","男"],
                    ["李四","女"]
                ]
            },
            {
                "sheetName": "st2",
                "data": [
                    ["课程", "分数"],
                    ["语文", 34],
                    ["数学", 43]
                ]
            }
        ]
    }
}

from excel2db.com.util import fileTool
import openpyxl
filetool = fileTool.fileTool()

def generalDemoFile():
    for demoName in demo:
        filetool.createDir("./" + demoName, mode=1)
        filetool.writeOverFile("./" + demoName + "/__init__.py", "")
        filetool.writeOverFile("./" + demoName + "/" + demoName + ".py", demo[demoName]["file"])
        filetool.writeOverFile("./" + demoName + "/" + demoName + ".json", demo[demoName]["json"])

        # 生成一个 Workbook 的实例化对象，wb即代表一个工作簿（一个 Excel 文件）
        wb = openpyxl.Workbook()
        index = 1
        for sheet in demo[demoName]["excel"]:
            if index==1:
                ws=wb.active
                ws.title = sheet["sheetName"]
            else:
                wb.create_sheet(sheet["sheetName"])
                ws = wb[sheet["sheetName"]]

            index += 1

            for row in sheet["data"]:
                ws.append(row)

        wb.save("./" + demoName + "/" + demoName + ".xlsx")

if __name__ == "__main__":
    generalDemoFile()