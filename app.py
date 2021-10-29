from flask import Flask, jsonify, request

app = Flask(__name__)

toDOList = []
toDoItem = {}
toDoItem['name'] = "Изучить Flask"
toDoItem['priority'] = 1
toDOList.append(toDoItem)
toDOList.append(toDoItem)
toDOList.append(toDoItem)


@app.route('/')
def status():  # put application's code here
    status = ""
    for item in toDOList:
        status += f"name {item['name']}  &nbsp; &nbsp;" \
                  f" priority: {item['priority']} </br>"
    return status


@app.route('/get/<int:id>')
def getToDO(id):
    if 0 <= id < len(toDOList):
        item = toDOList[int(id)]
        return jsonify(item)
    else:
        return ""


@app.route('/set', methods=['POST'])
def set():
    data = request.json
    print(data)
    toDOList.append(data)
    return f"{data}", 200

if __name__ == '__main__':
    app.run()
