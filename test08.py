from easy_excel_util import Builder, ExportField


def xlsx():
    Builder.build_export(xlsx=True).sheet(
        index=0, data=weatehr_data, parse_map=dict(
        city=ExportField(index=0, col_name='城市', width=15), 
        meizu=ExportField(index=1, col_name='魅族', width=10), 
        xiaomi=ExportField(index=2, col_name='小米', width=10),
        hefeng=ExportField(index=3, col_name='和风', width=10)
        )
        ).do_export('/PYTHON/1.xlsx')


weatehr_data = [{'city': 2, 'meizu': "str(mz_temperature)", 'xiaomi': "str(xm_temperature)",'hefeng':"str(hef_temperature)"}]






weatehr_data1 = [{'city': 1, 'meizu': "str(mz_temperature)1", 'xiaomi': "str(xm_temperature)1",'hefeng':"str(hef_temperature)1"}]

weatehr_data += weatehr_data1

xlsx()