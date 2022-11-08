import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    catImg: null,
  },
  getters: {
    catImage (state) {
      return state.catImg
    }
  },
  mutations: {
    SAVE_CAT_IMAGE (state, data) {
      state.catImg = data
    }
  },
  actions: {
    getCatImg (context) {
      const catURL = "https://api.thecatapi.com/v1/images/search"
      axios({
        url: catURL,
        method: 'GET'
      })
      .then( res => {
        // console.log(res)
        const catImg = res.data[0].url
        context.commit('SAVE_CAT_IMAGE', catImg)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
