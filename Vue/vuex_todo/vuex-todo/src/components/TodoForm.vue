<template>
  <div>
    <input 
    type="text"
    v-model.trim="inputTodo"
    @keyup.enter="createTodo">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
    name: 'TodoForm',
    data() {
        return {
            inputTodo: null,
        }
    },
    methods: {
        createTodo() {
            if (this.inputTodo) {
                this.$store.dispatch('createTodo', this.inputTodo)
            }
            this.inputTodo = null
            
        }
    }
}
</script>

<style>

</style>