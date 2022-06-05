<template>
  <main class="contract">
      <hgroup class="contract-title">
          <h1>Contratos</h1>
      </hgroup>
      <p v-if="!contracts.length" class="contract-no">
          Aún no tienes ningun contrato :(
      </p>
      <ul class="contract-list">
          <li class="contract-list-item" v-for="contract in contracts" :key="contract.id">
              <cards-contracts 
                :contract="contract"
              />
          </li>
      </ul> 
  </main>
</template>

<script>
export default {
    layout: 'buyer',
    async asyncData({$axios, store}) {
        const req = await $axios.get('contract')
        const data = req.data
        
        const data_filtered = data.filter( el => el.buyer.toString() == store.state.auth.user.user_id)


        data_filtered.forEach( async function(e) {
            let reqs = await $axios.get(`users/seller/${e.seller}/`)

            e.seller = reqs.data
        })

        return {
            contracts: data_filtered
        }
    },
    beforeCreate() {
        const type = this.$store.state.auth.type

        if (!(type == 'B')) {
            this.$router.push('/')
        }
    },
    data() {
        return {
            contracts: [1,2,3,4,5]
        }
    }
}
</script>

<style lang="sass" scoped>
    .contract
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