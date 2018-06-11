#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Ranxf

import xlwt, xlrd

xls = xlwt.Workbook()
sheet = xls.add_sheet('sample')
sheet.write(0, 0, 'netcon')
sheet.write(0, 1, 'conw.net')
xls.save('sample.xls')


xls = xlrd.open_workbook('sample.xls')
sheet = xls.sheets()[0]
values = sheet.row_values(0)
print(values)
