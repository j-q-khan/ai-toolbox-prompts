// Example output: written by hand for the video to show the shape of the file. Claude Code was not run to make it; yours will differ.
// It keeps one bug on purpose for the video: pressing Enter with nothing typed adds an empty task.
const form = document.getElementById('task-form');
const input = document.getElementById('task-input');
const list = document.getElementById('task-list');
const count = document.getElementById('task-count');

let tasks = loadTasks();

function loadTasks() {
  try {
    return JSON.parse(localStorage.getItem('tasks')) || [];
  } catch (error) {
    return [];
  }
}

function saveTasks() {
  try {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  } catch (error) {
    // This browser won't allow local storage, so the list works without saving.
  }
}

function showTasks() {
  list.replaceChildren();
  tasks.forEach((task, index) => {
    const item = document.createElement('li');
    if (task.done) {
      item.classList.add('done');
    }

    const box = document.createElement('input');
    box.type = 'checkbox';
    box.checked = task.done;
    box.addEventListener('change', () => {
      task.done = box.checked;
      saveTasks();
      showTasks();
    });

    const text = document.createElement('span');
    text.textContent = task.text;

    const remove = document.createElement('button');
    remove.textContent = 'Delete';
    remove.addEventListener('click', () => {
      tasks.splice(index, 1);
      saveTasks();
      showTasks();
    });

    item.append(box, text, remove);
    list.append(item);
  });

  const left = tasks.filter((task) => !task.done).length;
  count.textContent = left === 1 ? '1 task left' : left + ' tasks left';
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  tasks.push({ text: input.value, done: false });
  input.value = '';
  saveTasks();
  showTasks();
});

showTasks();
