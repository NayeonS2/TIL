<template>
  <div @click="onSelectVideo" class="video-list-item">
    <li>
        <img :src="videoThumbnails" alt="">
        <h3>{{ videoTitle | unescape }}</h3>
        <p>{{ videoDescription }}</p>

    </li>
    
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'VideoListItem',
    props: {
        video: Object,
    },
    computed: {
        videoTitle() {
            return this.video.snippet.title
        },
        videoDescription() {
            return this.video.snippet.description
        },
        videoThumbnails() {
            return this.video.snippet.thumbnails.medium.url
        },
    },
    methods: {
        onSelectVideo() {
            this.$emit('on-select-video', this.video)
        }
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