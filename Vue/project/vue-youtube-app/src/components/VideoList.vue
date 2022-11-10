<template>
  <div v-if="videoList.length">
    <ul>
        <VideoListItem
        v-for="video in videoList"
        :video="video"
        :key="video.id.videoId"
        @on-select-video="onSelectVideo"
    />
        
    </ul>
    
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'


export default {
    name: 'VideoList',
    props: {
        videoList: Array,
    },
    components: {
        VideoListItem,
    },
    methods: {
        onSelectVideo(video) {
            this.$emit('on-select-video', video)
        }
    }
}
</script>

<style>

</style>