<template>
  <div class="d-flex justify-content-evenly container pt-3">
    <div class="row row-cols-1 row-cols-md-3 g-4 justify-content-evenly">
        <MovieCard
        v-for="(movie,idx) in movieList"
        :key="idx"
        :movie="movie"
        :idx="idx"
        />


    </div>
    
  </div>
</template>

<script>

import MovieCard from '@/components/MovieCard'


export default {
    name: 'MovieView',
    data() {
        return {
  
        }
    },
    computed: {
        movieList() {
            return this.$store.state.movieList
        }
    },
    components:{
        MovieCard,
    },
   
}
</script>

<style>

</style>