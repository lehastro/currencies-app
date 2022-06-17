from func_Days_less10 import *

def func_for_days_more_than_10():
  for i in this_month:
    if 10<=i<=current_day:
        res = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={i}/{current_month}/{current_year}")
        with open ('course.xml', 'wb') as file:
            file.write(res.content)
            doc = minidom.parse("course.xml")
            root = doc.getElementsByTagName("ValCurs")[0]
            data = f"{i}.{current_month}.{current_year}"
            currency = doc.getElementsByTagName("Valute")
            for rate in currency:
              id = rate.getAttribute("ID")
              numcode1 = rate.getElementsByTagName("NumCode")[0]
              charcode1 = rate.getElementsByTagName("CharCode")[0]
              nominal1 = rate.getElementsByTagName("Nominal")[0]
              name1 = rate.getElementsByTagName("Name")[0]
              value1 = rate.getElementsByTagName("Value")[0]


              numcode=numcode1.firstChild.data
              charcode=charcode1.firstChild.data
              nominal=nominal1.firstChild.data
              name=name1.firstChild.data
              value=value1.firstChild.data
              def add_data_in_table():
                  add_data = "INSERT INTO currencies (data, id, numcode, charcode, nominal, name, value) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                  record= ( data, id, numcode, charcode, nominal, name, value)
                  db.cursor.execute(add_data, record)
              add_data_in_table()
