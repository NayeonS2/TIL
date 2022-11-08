<template>
  <div>
    <ul>
        <TodoListItem
        v-for="(todo, index) in todoList"
        :key="index"
        :todo="todo"
        />
    </ul>
    
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
export default {
    name: 'TodoList',
    components: {
        TodoListItem, 
    },
    computed: {
        todoList() {
            return this.$store.getters.todoList
        },
        
    }
}
</script>

<style>

</style>