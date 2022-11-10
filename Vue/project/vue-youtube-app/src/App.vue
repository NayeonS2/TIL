<template>
  <div id="app">
    <h1>My first youtube project</h1>
    <TheSearchBar
    @on-keyword-enter="onKeywordEnter"
    />

    <VideoDetail
    :video="video"
    />
    <hr>

    <VideoList
    :videoList="videoList"
    @on-select-video="onSelectVideo"
    />
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'


export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      videoList: [],
      video: null
    }
  },
  methods: {
    onKeywordEnter(videoList) {
      this.videoList = videoList
    },
    onSelectVideo(video) {
      this.video = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
