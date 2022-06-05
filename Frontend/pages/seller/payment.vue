<template>
  <main class="payment">
      <hgroup class="payment-title">
          <h1>Pagos</h1>
      </hgroup>
      <p v-if="!payments.length" class="payment-no">
          Aún no tienes ningun pago asociado a un contrato :(
      </p>
      <ul class="payment-list">
          <li class="payment-list-item" v-for="payment in payments" :key="payment">
              <cards-payments-seller />
          </li>
      </ul> 
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
            payments: [1,2,3,4,5]
        }
    }
}
</script>

<style lang="sass" scoped>
    .payment
        padding: 2rem
        max-width: 1200px

        &-no
            background: #e5d87f
            text-align: center
            font-weight: bold
            padding: 1rem 2rem

        &-list
            display: flex
            flex-wrap: wrap
            gap: 1rem
</style>