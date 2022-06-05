<template>
  <section class="box">
      <cards-vehicles :id="contract.vehicle" class="box-card" />
      <section class="box-card-user" >
          <template v-if="contract.buyer.first_name">
            <span>Nombre: {{contract.buyer.first_name}}</span>
            <span>Teléfono: {{contract.buyer.phone}}</span>
            <span>Email: {{contract.buyer.email}}</span>
            <span>DNI: {{contract.buyer.doc_identifier}}</span>
          </template>
          <template v-else>
            <span>Nombre: {{contract.seller.first_name}}</span>
            <span>Teléfono: {{contract.seller.phone}}</span>
            <span>Email: {{contract.seller.email}}</span>
            <span>DNI: {{contract.seller.doc_identifier}}</span>
          </template>
          
      </section>
      <section class="box-card-status" >
          <span v-if="status == 'P'">No pagado</span>
          <span v-else>Pagado</span>
      </section>
  </section>
</template>

<script>
export default {
    props: {
        contract: {
            type: Object,
            required: false,
            default: () => ({})
        }
    },
}
</script>

<style lang="sass" scoped>
    .box
        max-width: 100%
        border-radius: 1rem
        box-shadow: 0 0 10px #ccc
        padding: 1rem

        display: grid
        gap: .5rem
        grid-template-columns: auto
        grid-template-rows: 1fr
        overflow: hidden
        cursor: pointer

        @media screen and (min-width: 480px)
            grid-template-columns: repeat(3, 1fr)
            
            &-card
                &-user
                    grid-column: 2 / 3
                    grid-row: 1
                    border-bottom: 0 !important

        &-card
            margin: auto

            &-user
                display: grid
                border-bottom: 1px solid #ccc

            &-status
                width: fit-content
                height: fit-content
                margin: auto
                background: #e5d87f
                padding: .5rem
</style>