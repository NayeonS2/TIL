<template>
  <div>
    <h1>오늘의 로또</h1>
    <button @click="pickNums">Lotto</button>
    <p>{{ nums }}</p>
  </div>
</template>

<script>
import _ from "lodash"
export default {
    name: 'TheLotto',
    data() {
    return {
        nums: '',
        }
    },
    methods: {
        pickNums() {
            const pickedNums = _.sampleSize(_.range(1,46), 6)
            this.nums = _.join(pickedNums, " ")
        }

    }
    }

</script>

<style>

</style>