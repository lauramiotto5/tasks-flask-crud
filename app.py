from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD: Create, Read, Update, Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1


# Create
@app.route('/tasks', methods=['POST'])
def create_task():
    # request: recupera informações
    global task_id_control
    # global: pega a referência que está fora do método
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'],
                    description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})


# Read
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
        # len(): conta o valor de quantos elementos têm
    }
    return jsonify(output)


# <int:id> parâmetro de rota: receber uma variável do usuário
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


# Update
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    # recupera o que o cliente enviou
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)

    return jsonify({"message": "Tarefa atualizada com sucesso"})


# Delete
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        print(t)
        if t.id == id:
            task = t
            break
        # break: para no momento em que a atividade foi encontrada
        # não gasta processamento atoa

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)  # <- só para desinvolvimento manual
