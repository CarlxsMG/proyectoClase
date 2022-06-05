<template>
  <main class="profile">
      <hgroup>
          <h1>Mi perfil</h1>
      </hgroup>
      <form-profile />
  </main>
</template>

<script>
export default {
    layout: 'seller',
    beforeCreate() {
        const type = this.$store.state.auth.type

        if (!(type == 'S')) {
            this.$router.push('/')
        }
    },
}
</script>

<style lang="sass" scoped>
    .profile
        padding: 2rem
</style>