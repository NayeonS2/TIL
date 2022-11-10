import Vue from 'vue'
import Vuex from 'vuex'
import _ from "lodash"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    menus: ['짜장면','짬뽕','비빔냉면','탕수육','냉면','볶음밥'],
    menu: null,
    numbers: null,
  },
  getters: {
  },
  mutations: {
    PICK_MENU(state) {
      state.menu = _.sample(state.menus)
    },
    PICK_NUMBERS(state) {
      state.numbers = _.sampleSize(_.range(1,46), 6)
    },
   
  },
  actions: {
  },
  modules: {
  }
})
