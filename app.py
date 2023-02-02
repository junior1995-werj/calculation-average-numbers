from flask import Flask, request

from calculation_average_nunbers.calculation import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def get_global_avg():

    list_nunber_initial, average = reader_file()

    if request.method == 'GET':
    
        return {
            "list_nunber_insert": list_nunber_initial,
            "mediana" : average
            }
    
    elif request.method == 'POST':  
        request_data = request.get_json()
        list_nunber_initial.append(int(request_data['new_number']))
        average = calculate_average(list_number=list_nunber_initial)
        
        writer_file(list_nunber_initial)

        return {
            "list_nunber_insert": list_nunber_initial,
            "mediana" : average
            }

    return {
        "list_nunber_insert": list_nunber_initial,
        "mediana" : average
        }
        
if __name__ == "__main__":
    app.run()