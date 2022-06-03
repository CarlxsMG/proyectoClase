<template>
  <section class="box">
      <cards-vehicles class="box-card" />
      <section class="box-card-user" >
          <span>Nombre: {{user.name}}</span>
          <span>Teléfono: {{user.phone}}</span>
          <span>Email: {{user.email}}</span>
          <span>DNI: {{user.dni}}</span>
      </section>
      <section class="box-card-status" >
          <span v-if="status == 'P'">No pagado</span>
          <span v-else>Pagado</span>
      </section>
  </section>
</template>

<script>
export default {
    data() {
        return {
            status: 'P',
            user: {
                name: 'Juan',
                phone: '674832609',
                email: 'carlosmartiguerre@gmail.com',
                dni: '23887095P'
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