<template>
  <div id="app">
    <h1><b>버튼 박스 제작</b></h1>
    <br>
    <div class="shadow p-3 mb-5 bg-body rounded">
      <h2><b>예약페이지</b></h2>
      <br>
      <br>
      <h3><b>시간 선택</b></h3>
      <br>
      <div style="width:500px; margin:auto;">
        <div style="display: flex;">
        <div v-for="(time, index) in times.slice(0,8)" :key="index">
        <button type="button" class="btn btn-light" @click="select">{{ time }}</button>
        </div>
      </div>
        
      <div style="display: flex;">
        <div v-for="(time, index) in times.slice(8,16)" :key="index">
        <button type="button" class="btn btn-light" @click="select">{{ time }}</button>
        </div>
      </div>

      <div style="display: flex;">
        <div v-for="(time, index) in times.slice(16,24)" :key="index">
        <button type="button" class="btn btn-light" @click="select">{{ time }}</button>
        </div>
      </div>

      <div style="display: flex;">
        <div v-for="(time, index) in times.slice(24,32)" :key="index">
        <button type="button" class="btn btn-light" @click="select">{{ time }}</button>
        </div>
      </div>
      </div>
      
      <hr>
      <span>선택시간 : {{ choices }}</span>
    </div>
   
    
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'App',
  data() {
    return {
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
  ],
  arr: [],
  cnt: 0,
  choices: null,

    }
  },
  methods: {
    select: function (event) {

      const buttons = document.querySelectorAll('button')
      
      
      if (this.cnt < 5) {
        if (this.arr.includes(event.target.textContent)) {
        this.arr.splice(_.indexOf(this.arr, event.target.textContent))
        event.target.setAttribute('class', 'btn btn-light') 
        this.cnt -= 1
      } else {
        this.arr.push(event.target.textContent)
        event.target.setAttribute('class', 'btn btn-primary') 
        this.cnt += 1
        
      }

      } else {
        alert('5타임까지만 신청할 수 있습니다.')
        


        for (const but of buttons) {
          if (but.getAttribute('class') === 'btn btn-primary') {

            but.setAttribute('class', 'btn btn-light')

          }
          
        }


        this.cnt = 0
        this.arr = []
        
        
      }
      
      this.choices = _.join(this.arr, "  ")
  
    },
  }
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
