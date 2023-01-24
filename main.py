from flask import request, make_response, send_file, Flask
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)
  
@app.route('/download_csv', methods=['GET', 'POST'])
def download_csv():
    try:
        os.remove('data.csv')
    except:
        pass
    data = request.get_json()
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv('data.csv', index=False)
    df = pd.read_csv('pincode.csv')
    df = df.fillna(0)
    df = df.astype(int)
    
    
    tamilnadu = df['tamilnadu'].tolist()
    south = df['south'].tolist()
    north = df['north'].tolist()
    
    
    df1 = pd.read_csv('data.csv')
    df1['weight'] = df1['weight'].astype(float)
    df1['pincode'] = df1['pincode'].astype(int)
    df1['mode'] = df1['mode'].astype(str)
    
    # create a new column in df1 called 'price'
    
    # create a df called df2 with col pincode, weight, mode, price
    df2 = pd.DataFrame(columns=['ccno','pincode', 'weight', 'mode', 'price'])
    
    for index, row in df1.iterrows():
    
        pincode = row['pincode']
        weight = row['weight']
        mode = row['mode']
        ccno = row['ccno']
    
        # print(pincode, weight, mode)
        print(mode)

        if pincode in tamilnadu:
            print('tamilnadu')
    
            if weight <= 1:
                print("weight 0-1", weight)
                df2 = df2.append({'ccno':ccno,'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': 30}, ignore_index=True)
            # elif  weight between 1-5  then 0.5 kg is 15rs
            elif weight  > 1 and weight <= 5:
                howMany = int(weight / 0.5)
                leftOver = weight % 0.5
                leftOver = weight - (howMany * 0.5)
                if leftOver > 0:
                    howMany = howMany + 1
                print("weight between 1-5", weight)
                print(howMany * 15)
                df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 15}, ignore_index=True)
             # weight between 5-10 then 0.5 kg is  11 rs
            elif weight  > 5 and weight <= 10:
                howMany = int(weight / 0.5)
                leftOver = weight % 0.5
                leftOver = weight - (howMany * 0.5)
                if leftOver > 0:
                    howMany = howMany + 1
                print("weight between 5-10", weight)
                print(howMany * 11)
                row['price'] = howMany * 11
                df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 11}, ignore_index=True)
            # weight between 10-15 then 0.5 kg is  9 rs
            elif weight  > 10 and weight <= 15:
                howMany = int(weight / 0.5)
                leftOver = weight % 0.5
                leftOver = weight - (howMany * 0.5)
                if leftOver > 0:
                    howMany = howMany + 1
                print("weight between 15-20", weight)
                print(howMany * 9)  
                row['price'] = howMany *9  
                df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 9}, ignore_index=True)
            # weight between 15-20 then 0.5 kg is  7.5 rs
            elif weight  > 15 and weight <= 20:
                howMany = int(weight / 0.5)
                leftOver = weight % 0.5
                leftOver = weight - (howMany * 0.5)
                if leftOver > 0:
                    howMany = howMany + 1
                print("weight between 15-20", weight)
                print(howMany * 7.5)
                row['price'] = howMany * 7.5
                df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 7.5}, ignore_index=True)
    
            # weight between 20-100 then 0.5 kg is  7 rs
            elif weight  > 20 and weight <= 100:
                howMany = int(weight / 0.5)
                leftOver = weight % 0.5
                leftOver = weight - (howMany * 0.5)
                if leftOver > 0:
                    howMany = howMany + 1
                print("weight between 20-100", weight)
                print(howMany * 7)   
                row['price'] = howMany * 7 
                df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 7}, ignore_index=True)
            else:
                df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': 0}, ignore_index=True)    
        elif pincode in south:
             print('south')
            
             if weight <= 1:
                 print("weight between 0-1", weight)
                 row['price'] = 40
                 df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': 40}, ignore_index=True)
             elif weight  > 1 and weight <= 5:
                 howMany = int(weight / 0.5)
                 leftOver = weight % 0.5
                 leftOver = weight - (howMany * 0.5)
                 if leftOver > 0:
                     howMany = howMany + 1
                 print("weight between 1-5", weight)
                 print(howMany * 20)
                 df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 20}, ignore_index=True)
            # weight between 5-10 then 0.5 kg is  17.5 rs
             elif weight  > 5 and weight <= 10:
                 howMany = int(weight / 0.5)
                 leftOver = weight % 0.5
                 leftOver = weight - (howMany * 0.5)
                 if leftOver > 0:
                     howMany = howMany + 1
                 print("weight between 5-10", weight)
                 print(howMany * 17.5)
                 df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 17.5}, ignore_index=True)
             # weight between 10-15 then 0.5 kg is  15 rs
             elif weight  > 10 and weight <= 15:
                 howMany = int(weight / 0.5)
                 leftOver = weight % 0.5
                 leftOver = weight - (howMany * 0.5)
                 if leftOver > 0:
                     howMany = howMany + 1
                 print("weight between 10-15", weight)
                 print(howMany * 15)
                 df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 15}, ignore_index=True)
             elif weight  > 15 and weight <= 20:
                 howMany = int(weight / 0.5)
                 leftOver = weight % 0.5
                 leftOver = weight - (howMany * 0.5)
                 if leftOver > 0:
                     howMany = howMany + 1
                 print("weight between 15-20", weight)
                 print(howMany * 13.5)
                 df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 13.5}, ignore_index=True)
             elif weight  > 20 and weight <= 100:
                 howMany = int(weight / 0.5)
                 leftOver = weight % 0.5
                 leftOver = weight - (howMany * 0.5)
                 if leftOver > 0:
                     howMany = howMany + 1
                 print("weight between 1-5", weight)
                 print(howMany * 12.5)
                 df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 12.5}, ignore_index=True)

        elif pincode in north:
            print('north')
            
            if mode == 'AR' or mode == 'AC':
                print('AR')
                if weight <= 1:
                    print("weight > 1", weight)
                    print(120)
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': 120}, ignore_index=True)
                elif weight > 1 and weight <= 5:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 1-5", weight)
                    print(howMany * 60)
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 60}, ignore_index=True)
                elif weight > 5 and weight <= 10:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 5-10", weight)
                    print(howMany * 57.5)
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 57.5}, ignore_index=True)
                elif weight > 10 and weight <= 25:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 10-25", weight)
                    print(howMany * 55)    
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 55}, ignore_index=True)
                elif  weight > 25 and weight <= 100:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 25-100", weight)
                    print(howMany * 52.5)   
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 52.5}, ignore_index=True)
            elif mode == "SF":
                print("SF ------------>")
                if weight < 1:
                    print("weight > 1", weight)
                    print(240)
                    row['price'] = 240
                elif weight > 2.5 and weight <= 5:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 1-5", weight)
                    print(howMany * 40)
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 40}, ignore_index=True)
                elif weight > 5 and weight <= 10:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 5-10", weight)
                    print(howMany * 30)
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 30}, ignore_index=True)
                elif weight > 10 and weight <= 15:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 10-15", weight)
                    print(howMany * 27.5)    
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 27.5}, ignore_index=True)
                elif  weight > 15 and weight <= 20:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 25-100", weight)
                    print(howMany * 25)  
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 25}, ignore_index=True)
                elif  weight > 20 and weight <= 25:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 20-25", weight)
                    print(howMany * 22.5)
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 22.5}, ignore_index=True)
                elif weight > 25 and weight <= 100:
                    howMany = int(weight / 0.5)
                    leftOver = weight % 0.5
                    leftOver = weight - (howMany * 0.5)
                    if leftOver > 0:
                        howMany = howMany + 1
                    print("weight between 25-100", weight)
                    print(howMany * 20)   
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': howMany * 20}, ignore_index=True)
                else:
                    print("SFFFF found------------>", pincode, mode, weight)    
                    df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': 0}, ignore_index=True)
            else:
                        print("SFFFF found------------>", pincode, mode, weight)  
                        df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': 0}, ignore_index=True)    
        else:
            print("not found------------>", pincode, mode, weight)
            df2 = df2.append({'ccno':ccno,'pincode': pincode, 'weight': weight, 'mode': mode, 'price': 0}, ignore_index=True)
        
        # sum of price 
        
    total = df2['price'].sum()
        # append total price to df2
    df2 = df2.append({'ccno':"Total",'pincode': "", 'weight': "", 'mode': "", 'price': total}, ignore_index=True)
    df2.to_csv("output.csv", index=False)
    path = "output.csv"
    return send_file(path, as_attachment=True) 
 
@app.route('/download_file', methods=['GET', 'POST'])
def download_file():
    path = "output.csv"
    return send_file(path, as_attachment=True) 


    
if        __name__ == "__main__":
    app.run(debug=True)
