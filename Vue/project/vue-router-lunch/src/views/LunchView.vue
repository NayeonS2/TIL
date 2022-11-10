<template>
  <div>
    <h1>Lunch</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p v-if="menu">{{ menu }}</p>
    <button v-if="menu" @click="pickLotto(menu)">Lotto 뽑으러가기</button>
  </div>
</template>

<script>
export default {
    name: 'LunchView',
    data() {
        return {
            menu : null,
        }
    },
    computed: {
        pickedMenu() {
            return this.$store.state.menu
        }
    },
    methods: {
        pickLunch() {
            this.$store.commit('PICK_MENU')
            this.menu = this.pickedMenu
        },
        pickLotto(menu) {
            this.$router.push({ name:'lotto', params:{menu}})
        }
    }
}
</script>

<style>

</style>