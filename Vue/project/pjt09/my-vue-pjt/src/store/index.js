import Vue from 'vue'
import Vuex from 'vuex'
import _ from "lodash"

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    movieList: null,
    randomMovieTitle: null,
    randomMovieImg: null,
    wishes: [],
    weather: null,
    weatherType: null,
    randomGenre: null,
  },
  getters: {
    wishList (state) {
      return state.wishes
    },
  },
  mutations: {
    MOVIE_LIST(state, movieList) {
      state.movieList = movieList
    },
    RANDOM_MOVIE(state) {
      const randomMovie = _.sample(state.movieList)
      state.randomMovieTitle = randomMovie.title
      state.randomMovieImg = randomMovie.poster_path
      state.randomGenre = randomMovie.genre_ids
    },
    CREATE_WISH(state, data) {
      const wish = {
        title: data,
        isCompleted: false,
      }
      state.wishes.push(wish)
    },
    UPDATE_WISH(state, data) {
      state.wishes = state.wishes.map((wish) => {
        if (wish === data) {
          wish.isCompleted = !wish.isCompleted
        }
        return wish
      })
    },
    PICK_WISH(state, data) {
      const pickWish = {
        title: data,
        isCompleted: false,
      }

      
      let flag = 0

      for (const x of state.wishes) {
        if (x.title === pickWish.title) {
          flag = 1
          alert("이미 찜하셨습니다 ❗")
        } 
      }

      if (flag===0) {
        state.wishes.push(pickWish)
      }
      
    },
    TODAY_WEATHER(state, data) {
      
      state.weather = data.weather
      state.weatherType = data.weatherType
      console.log(data.weather, data.weatherType)
    }
  },
  actions: {
    createWish(context, data) {
      context.commit('CREATE_WISH', data)
    },
    updateWish(context, data) {
      context.commit('UPDATE_WISH', data)
    },
    pickWish(context, data) {
      context.commit('PICK_WISH', data)
    }
  },
  modules: {
  }
})
