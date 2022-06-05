<template>
  <main class="trade">
      <hgroup class="trade-title">
          <h1>Peticiones</h1>
      </hgroup>
      <p v-if="!trades.length" class="trade-no">
          Aún no tienes ninguna petición :(
      </p>
      <ul class="trade-list">
          <li class="trade-list-item" v-for="trade in trades" :key="trade.id">
              <cards-trades 
                :status="trade.status"
              />
          </li>
      </ul> 
  </main>
</template>

<script>
export default {
    layout: 'seller',
    async asyncData({$axios, store}) {
        const req = await $axios.get('contract')
        const data = req.data
        const data_filtered = data.filter( el => el.seller.toString() == store.state.auth.user.user_id && el.status != 'C')

        return {
            trades: data_filtered
        }
    },
    beforeCreate() {
        const type = this.$store.state.auth.type

        if (!(type == 'S')) {
            this.$router.push('/')
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