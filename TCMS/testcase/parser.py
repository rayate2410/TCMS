import xlrd
import json


class ParseXls():
    def __init__(self):
        self.columns = ["title","steps","expcted_result"]
        
    def parse_xls(self,source_file):
        xls_workbook = xlrd.open_workbook("localization.xlsx")
        xls_sheet = xls_workbook.sheet_by_index(0)
        for rn in range(xls_sheet.nrows):
            for cn in range(xls_sheet.ncols-1):
                key = xls_sheet.cell(rn,0).value