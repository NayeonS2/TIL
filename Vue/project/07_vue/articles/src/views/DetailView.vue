<template>
  <div>
    <h1>Detail</h1>
  </div>
</template>

<script>
export default {
    name: 'DetailView',
    data() {
        return {
            article: null,
        }
    },
    computed: {
        articles() {
            return this.$store.state.articles
        }
    },
    methods: {
        getArticleById() {
            // url로 오는 id ( 문자열 )저장
            const id = this.$route.params.id
            for (const article of this.articles) {
                if (article.id === Number(id)) {
                    this.article = article
                    break

                }
            }
        }
    }
}
</script>

<style>

</style>