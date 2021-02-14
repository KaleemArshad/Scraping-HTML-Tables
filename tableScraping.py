from bs4 import BeautifulSoup
import pandas as pd
import os

folderPath = input(
    'Please Paste here the Absolute Path to the Folder not to the HTML File as you done before \n and dont forgot to replace \ with / in the path \n > ')

for root, dirs, files in os.walk(folderPath, topdown=True):
    for fileName in files:
        if fileName.endswith(".html"):
            soup = BeautifulSoup(
                open(os.path.join(root, fileName)).read(), 'lxml')

            one_list = []
            sec_list = []
            third_list = []
            fourth_list = []
            fifth_list = []
            sixth_list = []
            sev_list = []
            eight_list = []
            nine_list = []
            ten_list = []
            elev_list = []
            twe_list = []
            thir_list = []
            fourteen_list = []
            fif_list = []
            six_list = []
            seven_list = []
            eighteen_list = []
            ninteen_list = []

            print('Scraping Required Information Please Wait...')

            for a in soup.select('.inActiveLink .grayBorder:nth-child(1)'):
                one = a.text
                one_list.append(one)

            for row in soup.select('.inActiveLink .grayBorder:nth-child(4)'):
                sec = row.text
                sec_list.append(sec)

            for b in soup.select('.inActiveLink .grayBorder:nth-child(5)'):
                third = b.text
                third_list.append(third)

            for c in soup.select('.inActiveLink .grayBorder:nth-child(6)'):
                four = c.text
                fourth_list.append(four)

            for d in soup.select('.inActiveLink .grayBorder:nth-child(7)'):
                five = d.text
                fifth_list.append(five)

            for e in soup.select('.inActiveLink .grayBorder:nth-child(8)'):
                sixth = e.text
                sixth_list.append(sixth)

            for f in soup.select('.inActiveLink .grayBorder:nth-child(9)'):
                sev = f.text
                sev_list.append(sev)

            for g in soup.select('.inActiveLink .grayBorder:nth-child(10)'):
                ei = g.text
                eight_list.append(ei)

            for h in soup.select('.inActiveLink .grayBorder:nth-child(11)'):
                ni = h.text
                nine_list.append(ni)

            for i in soup.select('.inActiveLink .grayBorder:nth-child(12)'):
                te = i.text
                ten_list.append(te)

            for j in soup.select('.inActiveLink .grayBorder:nth-child(13)'):
                el = j.text
                elev_list.append(el)

            for k in soup.select('.inActiveLink .grayBorder:nth-child(14)'):
                twe = k.text
                twe_list.append(twe)

            for l in soup.select('.inActiveLink .grayBorder:nth-child(15)'):
                th = l.text
                thir_list.append(th)

            for m in soup.select('.inActiveLink .grayBorder:nth-child(16)'):
                fo = m.text
                fourteen_list.append(fo)

            for n in soup.select('.inActiveLink .grayBorder:nth-child(17)'):
                fi = n.text
                fif_list.append(fi)

            for o in soup.select('.inActiveLink .grayBorder:nth-child(18)'):
                sixteen = o.text
                six_list.append(sixteen)

            for p in soup.select('.inActiveLink .grayBorder:nth-child(19)'):
                seven = p.text
                seven_list.append(seven)

            for q in soup.select('.inActiveLink .grayBorder:nth-child(20)'):
                eighteen = q.text
                eighteen_list.append(eighteen)

            for r in soup.select('.inActiveLink .grayBorder:nth-child(21)'):
                niniteen = r.text
                ninteen_list.append(niniteen)

            print()
            print('Scraping Done')

            data = {
                "'מס": one_list,
                "פע'": sec_list,
                "שם": third_list,
                "ישוב": fourth_list,
                "שכונה": fifth_list,
                "כתובת": sixth_list,
                "חדרים": sev_list,
                "סוג": eight_list,
                "שטח": nine_list,
                "קומה": ten_list,
                "מחיר": elev_list,
                "טלפון": twe_list,
                "תאריך עדכון מערכת": thir_list,
                "שעת עדכון מערכת": fourteen_list,
                "ת. עדכון": fif_list,
                "מדיה": six_list,
                "מעלית": seven_list,
                "הערות": eighteen_list,
                "תאריך רישום במערכת": ninteen_list
            }

            print()
            Output_File = input('Please Enter the Name of File(Output): > ')
            df = pd.DataFrame(data)
            df.to_csv(f"{Output_File}.csv", index=False)

            print('All Done')
