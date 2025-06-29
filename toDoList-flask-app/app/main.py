from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # loop.index in Jinja starts at 1, so subtract 1
    idx = task_id - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
    return redirect(url_for('index'))

@app.route('/delete_all', methods=['POST'])
def delete_all_tasks():
    tasks.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)