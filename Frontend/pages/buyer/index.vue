<template>
  <main class="profile">
      <hgroup>
          <h1>Mi perfil</h1>
      </hgroup>
      <form-profile
        :type_profile="'buyer'"
      />
  </main>
</template>

<script>
export default {
    layout: 'buyer',
    beforeCreate() {
        const type = this.$store.state.auth.type

        if (!(type == 'B')) {
            this.$router.push('/')
        }
    },
}
</script>

<style lang="sass" scoped>
    .profile
        padding: 2rem
</style>