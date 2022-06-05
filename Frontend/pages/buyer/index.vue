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
    layout: 'buyer',
    beforeCreate() {
        const user = this.$store.state.user
        
        if (!(user?.type == 'B')) {
            this.$router.push('/')
        }
    },
}
</script>

<style lang="sass" scoped>
    .profile
        padding: 2rem
</style>