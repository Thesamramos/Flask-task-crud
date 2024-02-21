from flask import Flask, request,jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"mensagem": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": tasks_list,
        "total_tasks": len(tasks_list)
    }
    return jsonify(output)

@app.tpute('/tasks/<int:id>', method=['GET'])
def get_task(id):
    task = none
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"mensagem": "Não foi possível encontrar a atividade"}), 404

if __name__ == '__main__':
    app.run(debug=True)