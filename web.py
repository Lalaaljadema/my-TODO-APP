import streamlit as st
import functions


todos=functions.get_todos('todos.txt')
c_todos= functions.get_todos('completed_todos.txt')
st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state['new_todo'] + '\n' #dictionary syntax has key= new_todo
    todos.append(todo)
    functions.write_todos('todos.txt',todos)

todos = functions.get_todos('todos.txt')

st.title("My Todo App")
st.subheader("Todo List")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox= st.checkbox(todo, key=todo) #todo checked
    if checkbox:
        todo_completed= todos.pop(index)  #remove the todo
        functions.write_todos('todos.txt',todos)
        del st.session_state[todo]
        c_todos.append(todo_completed+'\n')
        functions.write_todos('completed_todos.txt',c_todos)
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo..", on_change=add_todo, key='new_todo')

st.subheader("Completed Todos")
for c_todo in c_todos:
    st.checkbox(c_todo,key= c_todo)
