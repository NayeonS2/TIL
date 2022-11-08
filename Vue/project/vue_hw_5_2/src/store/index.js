import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  getters: {
    getCounter (state) {
      return state.counter
    }
  },
  mutations: {
    SAVE_COUNTER (state, data) {
      state.counter = data
    }
  },
  actions: {
    saveCnt (context, data) {
      // 전달되는 데이터를 저장하려면 mutation 호출
      context.commit('SAVE_COUNTER', data)
    }
  },
  modules: {
  }
})
