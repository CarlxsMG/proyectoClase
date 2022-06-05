<template>
  <main>
    <Header />
    <Nuxt />
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

<style>

</style>