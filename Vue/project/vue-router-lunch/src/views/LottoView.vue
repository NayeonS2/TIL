<template>
  <div>
    <h1>{{ this.$route.params.menu }}먹고</h1>
    <h1>Lotto 추첨</h1>
    <button @click="pickNumbers">Pick Numbers</button>
    <p v-if="numbers">{{ numbers }}</p>
    <button v-if="numbers" @click="toLunch">처음으로</button>

  </div>
</template>

<script>
export default {
    name: 'LottoView',
    data() {
        return {
            numbers: null,
        }
    },
    computed: {
        pickedNumbers() {
            return this.$store.state.numbers
        }
    },
    methods: {
        pickNumbers() {
            this.$store.commit('PICK_NUMBERS')
            this.numbers = this.pickedNumbers

        },
        toLunch() {
            this.$router.push({ name:'lunch'})
        }
    }

}
</script>

<style>

</style>