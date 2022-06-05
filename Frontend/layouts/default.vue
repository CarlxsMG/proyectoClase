<template>
  <main>
    <Header />
    <section >
        <h1>ERROR 404</h1>
    </section>
    <popup-login v-show="showPopup" />
    <Footer />
  </main>
</template>

<script>
export default {
  computed: {
    showPopup(){
      return this.$store.state.popup.open
    }
  }
}
</script>

<style lang="sass" scoped>
    section
        display: grid
        min-height: calc( 100vh - 74px)

        h1
            font-size: 3rem
            text-align: center
            height: fit-content
            margin: auto
</style>