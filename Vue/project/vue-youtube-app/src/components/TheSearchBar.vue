<template>
  <div>
    <input 
    type="text"
    @keyup.enter="onKeywordEnter"
    >
  </div>
</template>

<script>

import axios from 'axios'

const API_KEY = 'AIzaSyCzV5aiqbmMpV8r7Xwdi8yGjm3MFD-MDok'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
    name: 'TheSearchBar',
    methods: {
        onKeywordEnter(event) {
            const keyword = event.target.value
            const config = {
                params: {
                    part: 'snippet',
                    type: 'video',
                    q: keyword,
                    key: API_KEY,
                },
            }
            axios.get(API_URL,config)
            .then(res => {
                const videoList = res.data.items
                this.$emit('on-keyword-enter', videoList) 
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>

<style>

</style>