<template>
  <section class="box">
      <section class="box-card-section" >
          <NuxtLink class="box-card-contract" to="/seller/contract">
            <span >
                Contrato ID: {{contract.id}}
            </span>      
          </NuxtLink>
          <span class="box-card-status" v-if="status == 'P'">No pagado</span>
          <span class="box-card-status" v-else>Pagado</span>
      </section>
  </section>
</template>

<script>
export default {
    data() {
        return {
            status: 'P',
            contract: {
                id: 1
            }
        }
    }
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
            
            
            &-card
                &-user
                    grid-column: 2 / 3
                    grid-row: 1
                    border-bottom: 0 !important

        &-card
            margin: auto

            &-section
                display: grid
                gap: 1rem

            &-contract
                margin: auto
                text-decoration: underline
                color: #000
                cursor: pointer

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