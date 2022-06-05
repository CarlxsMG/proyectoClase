<template>
  <main class="vehicle">
      <hgroup class="vehicle-title">
          <h1>Tus vehiculos</h1>
      </hgroup>
      <p v-if="!vehicles.lenght" class="vehicle-no">
          Aún no tienes ningun vehiculo :(
      </p>
      <ul class="vehicle-list">
          <li class="vehicle-list-item">
              <cards-vehicles />
          </li>
      </ul>
  </main>
</template>

<script>
export default {
    layout: 'seller',
    async asyncData() {
        const req = await this.$axios.get('seller/vehicle')

        console.log(req)
    },
    beforeCreate() {
        const type = this.$store.auth.state.type
        console.log(type)
        if (!(type == 'S')) {
            // this.$router.push('/')
        }
    },
    data() {
        return {
            vehicles: []
        }
    }
}
</script>

<style lang="sass" scoped>
    .vehicle    
        padding: 2rem

        &-no
            background: #e5d87f
            text-align: center
            font-weight: bold
            padding: 1rem 2rem

        &-list
            display: grid
            justify-content: center

            &-item
                margin: auto
    
            @media screen and (min-width: 768px)
                grid-template-columns: repeat(2, 1fr)


            @media screen and (min-width: 1024px)
                grid-template-columns: repeat(3, 1fr)
                justify-content: space-evenly

            @media screen and (min-width: 1200px)
                grid-template-columns: repeat(4, 1fr)
                justify-content: space-evenly
        
</style>