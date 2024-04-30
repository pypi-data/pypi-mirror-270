# -*- coding:utf8 -*-
"""
##执行mainTitle级别转换
"""
from excel2db import cheakConf, scale
from com.util.coordinate import coordinate

class mainTitle:
    def __init__(self, value, conf):

        """
        mainTitle级别操作
        :param value: 变量文件
        :param conf: mainTitle级别配置（清洗前）
        """
        self.value = value
        cheakConf.mainTitleConf(self.value, conf) ##获取mainTitle级别配置(清洗后)

    def mainTitle(self):
        ##初始化mainTitle坐标集
        mainTitleCoord = coordinate(self.value.mainTitlePosition)
        ##判断标题行是否存在
        if mainTitleCoord.STATUS: ##若不存在
            for i in range(mainTitleCoord.columns): ##生成临时字段名
                self.value.columnsType["columns"+str(i)] = "str"
            return None

        ##若标题行存在
        ##将所有标题转换为字符串
        for i in range(mainTitleCoord.start[0] - 1, mainTitleCoord.start[0] + mainTitleCoord.rows - 1):
            for j in range(mainTitleCoord.start[1] - 1, mainTitleCoord.start[1] + mainTitleCoord.columns - 1):
                if self.value.sheetData.iloc[i,j] != self.value.sheetData.iloc[i,j]:
                    self.value.sheetData.iloc[i, j] = ""
                elif not isinstance(self.value.sheetData.iloc[i,j], str):
                    self.value.sheetData.iloc[i,j] = str(self.value.sheetData.iloc[i,j])

        ##调整scale级别
        if "scaleList" in self.value.mainTitleConfDown:
            scaleConfList = cheakConf.combinScaleConf(self.value, self.value.mainTitleConfDown["scaleList"], self.value.mainTitleConfDown, self.value.mainTitlePosition, mainTitleCoord)  ##scale级别配置文件合并
            for scaleConf in scaleConfList:
                scaleManager = scale.scale(self.value, scaleConf)
                scaleManager.scale()

        ##获取mainTitle级别数据
        self.value.mainTitleData = self.value.sheetData.iloc[
                                mainTitleCoord.start[0] - 1: mainTitleCoord.start[0] + mainTitleCoord.rows - 1,
                                mainTitleCoord.start[1] - 1: mainTitleCoord.start[1] + mainTitleCoord.columns - 1
                                ]

        ##形成columnsType
        for i in self.value.mainColumnIndex:
            code = self.value.numberToCode(i+1) ##数字转字母
            if code in self.value.mainTitleConf["titleByID"]:
                title = self.value.mainTitleConf["titleByID"][code]
            else:
                title = ""
                for j in self.value.titleRowIndex:
                    a = self.value.sheetData.iloc[j, i]
                    if a != a: ##判断是否为nan值
                        title += ''
                    elif not isinstance(a, str):
                        title += str(a)
                    else:
                        title += a
                    # title += a

            if title in self.value.columnsType or title == "":
                index = 0
                while True:
                    index += 1
                    titleTemp = title + "_" + str(index)
                    if titleTemp not in self.value.columnsType:
                        break
                title = titleTemp

            self.value.columnsType[title] = ["str", i]
