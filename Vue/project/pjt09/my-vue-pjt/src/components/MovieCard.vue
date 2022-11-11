<template>
  

    <div class="card col m-2 p-0" style="width: 18rem;">
        <img :src="moviePoster" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title fw-semibold">{{ movieTitle }}</h5>
            <p class="card-text trunc">{{ movieOverview }}</p>
        </div>
    </div>

  
</template>

<script>
export default {
    name: 'MovieCard',
    props: {
        movie: Object,
        idx: Number,
    },
    computed: {
        movieTitle() {
           
            return this.movie.title
        },
        moviePoster() {
            const posterURL = this.movie.poster_path
           
            return  `https://image.tmdb.org/t/p/w220_and_h330_face${posterURL}`
        },
        movieOverview() {
            return this.movie.overview
        }
    }
}
</script>

<style>
.trunc {
    overflow:hidden;
    display:-webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    white-space: normal;
    width: 240px;
 
  
}
</style>