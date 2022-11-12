<template>
  <div id="app">
    <nav class="navbar bg-primary text-dark bg-opacity-10 p-2 mb-5">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img src="https://www.ssafy.com/swp_m/images/common/logo3.png" alt="Logo" width="50" height="36" class="d-inline-block align-text-top">

        </a>
        <div class="d-flex container justify-content-end m-0 mt-2">
          <ul class="row fs-4" style="width:450px;">
            <li class="col"><router-link :to="{ name: 'MovieView' }" @click.native ="getData">Movie </router-link></li>
            <li class="col"><router-link :to="{ name: 'RandomView' }" @click.native="[randomMovie(),todayWeather()]">Random   </router-link></li>
            <li class="col"><router-link :to="{ name: 'WatchListView' }">WatchList</router-link></li>
          </ul>
          

        </div>
        
      </div>
    </nav>

    
    <router-view/>
  </div>
</template>

<script>

import axios from 'axios'

const API_KEY = '812e384969b0b5de7cadaa5e861f286d'
const WEATHER_KEY = '814d648a20fbc0b72d481f655d40a075'

export default {
  name: 'app',
  methods: {
    getData(event) {
      event.preventDefault()

      axios({
            method: 'get',
            url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}`
        })
        .then(res => {
            const movieList = res.data.results
            this.$store.commit('MOVIE_LIST', movieList)
        })
        .catch(err => {
            console.log(err)
        })
    },
    randomMovie() {
      axios({
            method: 'get',
            url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}`
        })
        .then(res => {
            const movieList = res.data.results

            const weatherMovieList = []

            const weather = this.$store.state.weatherType



            if (weather === "Clear") {
              for (const movie of movieList) {
                if (movie.genre_ids.includes(10402)|| movie.genre_ids.includes(10749)) {
                  weatherMovieList.push(movie)
                } 
              }
            } else if (weather === "Snow") {
              for (const movie of movieList) {
                if (movie.genre_ids.includes(10751)|| movie.genre_ids.includes(18)) {
                  weatherMovieList.push(movie)
                } 
              }

            } else if (weather === "Rain") {
              for (const movie of movieList) {
                if (movie.genre_ids.includes(27)|| movie.genre_ids.includes(9648) || movie.genre_ids.includes(53)) {
                  weatherMovieList.push(movie)
                } 
              }
            } else {
              for (const movie of movieList) {
                
                  weatherMovieList.push(movie)
                
              }
            }

            this.$store.commit('MOVIE_LIST', weatherMovieList)
            this.$store.commit('RANDOM_MOVIE')
        })
        .catch(err => {
            console.log(err)
        })

    },
    
    todayWeather() {

      axios({
        method: 'get',
        url: `https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&appid=${WEATHER_KEY}`
      })
      .then(res => {
        const weatherType = res.data.weather[0].main
        const weather = res.data.weather[0].description
        const weatherInfo = {weatherType,weather}
        this.$store.commit('TODAY_WEATHER', weatherInfo)
       
      })
      .catch(err => {
        console.log(err)
      })

    }
      


      
      
      
    
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');



#app {
  font-family: 'Gowun Dodum', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #4f86fc;
}

ul li{
  display: inline-block;
}

a {
  text-decoration: none;
}
</style>
