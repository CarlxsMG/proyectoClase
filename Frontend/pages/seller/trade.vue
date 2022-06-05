<template>
  <main class="trade">
      <hgroup class="trade-title">
          <h1>Peticiones</h1>
      </hgroup>
      <p v-if="!trades.length" class="trade-no">
          Aún no tienes ninguna petición :(
      </p>
      <ul class="trade-list">
          <li class="trade-list-item" v-for="trade in trades" :key="trade">
              <cards-trades />
          </li>
      </ul> 
  </main>
</template>

<script>
export default {
    layout: 'seller',
    beforeCreate() {
        const user = this.$store.state.user
        
        if (!(user?.type == 'S')) {
            this.$router.push('/')
        }
    },
    data() {
        return {
            trades: [1,2,3,4,5]
        }
    }
}
</script>

<style lang="sass" scoped>
    .trade
        padding: 2rem
        max-width: 1200px

        &-no
            background: #e5d87f
            text-align: center
            font-weight: bold
            padding: 1rem 2rem

        &-list
            display: grid
            gap: 1rem
</style>