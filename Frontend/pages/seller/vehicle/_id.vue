<template>
  <main class="vehicle">
      <hgroup class="vehicle-title">
          <h1 v-if="newItem">Nuevo vehiculo</h1>
          <h1 v-else>Editar vehiculo</h1>
      </hgroup>
      <p v-if="newItem" class="vehicle-guide">
          Introduzca los campos correspondientes para publicar su vehiculo!
      </p>
      <p v-else class="vehicle-guide">
          Edite los campos que prefiera!
      </p>

      <form-vehicle class="vehicle-form"/>
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
    data() {
        return {
            newItem: this.$route.params.id
        }
    }
}
</script>

<style lang="sass" scoped>

.vehicle    
        padding: 2rem

        &-guide
            background: #e5d87f
            text-align: center
            font-weight: bold
            padding: 1rem 2rem

</style>