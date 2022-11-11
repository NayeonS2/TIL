<template>
    <div>
        <h3 v-if="this.$store.state.randomMovieImg" class="fs-3">{{ weatherDesc }} 날씨에는 이런 영화 어떠세요~?!❤</h3>
   
        <button v-if="this.$store.state.randomMovieImg" type="button" class="btn btn-primary mb-2 mt-3 fs-5" @click="pickWish(randomMovieTitle)" style="width: 18rem;">나중에 볼래 ⭐</button>
        <div v-if="this.$store.state.randomMovieImg" class="m-auto card col m-2 p-0" style="width: 18rem;">
        
        
        
        
        <img :src="randomMovieImg" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title fw-bold">{{ randomMovieTitle }}</h5>
           
        </div>
    </div>
    </div>
    


</template>

<script>
export default {
    name: 'RandomView',
    computed: {
        randomMovieTitle() {
            
            return this.$store.state.randomMovieTitle
        },
        randomMovieImg() {
            const posterURL = this.$store.state.randomMovieImg
           
            return  `https://image.tmdb.org/t/p/w220_and_h330_face${posterURL}`
           
        },
        randomGenre() {
            return this.$store.state.randomGenre
        },
        weatherType() {
            return this.$store.state.weatherType
        },
        weatherDesc() {
            return this.$store.state.weather
        }
   
    },
    methods: {
        pickWish(data) {
            this.$store.dispatch('pickWish',data)
        }
    }
}
</script>

<style>

</style>