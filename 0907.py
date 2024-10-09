# from easy_excel_util import Builder, ExportField

  
# data = [{'城市': 1, '魅族': '姓名1', '小米': 18,'和风':1}]

# Builder.build_export(xlsx=True).sheet(
#     index=0, data=data, parse_map=dict(
#         city=ExportField(index=0, col_name='城市', width=5), 
#         meizu=ExportField(index=1, col_name='魅族', width=15), 
#         xiaomi=ExportField(index=2, col_name='小米', width=15),
#         hefeng=ExportField(index=2, col_name='和风', width=15)
#     )
# ).do_export('/PYTHON/1.xlsx')
# print("导出成功")
data = [{'城市': 1, '魅族': '姓名1', '小米': 18,'和风':1}]
data += data
print(data)