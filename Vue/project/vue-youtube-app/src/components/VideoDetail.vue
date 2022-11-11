<template>
  <div v-if="video">
    <iframe width="640" height="360" :src="videoURL" frameborder="0"></iframe>
    <hr>
    {{ videoTitle }}
    {{ videoDescription }}
  </div>
</template>

<script>

import _ from 'lodash'

export default {
    name: 'VideoDetail',
    props: {
        video: Object,
    },
    computed: {
        videoURL() {
            const videoId = this.video.id.videoId
            return `https://www.youtube.com/embed/${videoId}`
        },
        videoTitle() {
            return this.video.snippet.title
        },
        videoDescription() {
            return this.video.snippet.description
        },
    },
    filters: {
        unescape(rawText) {
            return _.unescape(rawText)
        }
    }
    
}
</script>

<style>

</style>