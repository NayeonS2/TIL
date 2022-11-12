<template>
  <div class="p-5" style="margin:auto; width:1200px;">
        <WatchListForm/>
        <WatchListItem
        v-for="(wish, index) in wishList"
        :key="index"
        :wish="wish"
        />
  </div>
</template>

<script>

import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
    name: 'WatchListView',
    components: {
        WatchListForm,
        WatchListItem,
    },
    computed: {
        wishList() {
            return this.$store.getters.wishList
        }
    }
}
</script>

<style>

</style>