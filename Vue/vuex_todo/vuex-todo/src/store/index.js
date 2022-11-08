import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [],
  },
  getters: {
    todoList (state) {
      return state.todos
    },
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted == true
      })
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    },
  },
  mutations: {
    CREATE_TODO (state, data) {
      const todo = {
        title: data,
        isCompleted: false,
      }
      state.todos.push(todo)
    },
    DELETE_TODO (state, data) {
      const index = state.todos.indexOf(data)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO (state, data) {
      state.todos = state.todos.map((todo) => {
        if (todo === data) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
  },
  actions: {
    createTodo (context, data) {
      context.commit('CREATE_TODO', data)
    },
    deleteTodo (context, data) {
      context.commit('DELETE_TODO', data)
    },
    updateTodo (context, data) {
      context.commit('UPDATE_TODO', data)
    },
  },
  modules: {
  }
})
