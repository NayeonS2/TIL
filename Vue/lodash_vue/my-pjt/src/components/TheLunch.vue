<template>
  <div>
    <h1>점심메뉴</h1>
   <button @click="pickOne">Pick one</button>
   <p>{{ picked }}</p>
  </div>
</template>


<script>
import _ from "lodash"
export default {
    name: 'TheLunch',
    data() {
    return {
        menus: ['짜장면','짬뽕','탕수육'],
        picked: '',
        
    }
  },
  methods: {
    pickOne() {
        const idx = _.sampleSize(_.range(0,this.menus.length), 1)
        this.picked = this.menus[idx]
    }
  }    
}
</script>

<style>

</style>