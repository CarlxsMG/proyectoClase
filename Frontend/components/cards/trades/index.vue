<template>
  <section class="box">
      <cards-vehicles class="box-card" :id="trade.vehicle" />
      <div class="box-buttons">
          <span class="box-buttons-status-p" v-if="status=='P'">
              Pendiente
          </span>
          <span class="box-buttons-status-c" v-else-if="status=='C'">
              Completa
          </span>
          <span class="box-buttons-status-r" v-else>
              Rechazada
          </span>
          <basic-button
            class="box-buttons-reject"
            :type="'button'"
            :text="'Rechazar'"
            @click.native="rejectTrade"
          />
          <basic-button
            class="box-buttons-accept"
            :type="'button'"
            :text="'Aceptar'"
            @click.native="acceptTrade"
          />
      </div>
  </section>
</template>

<script>
export default {
    props: {
        trade: {
            type: Object,
            required: true
        },
        item: {
            type: Object,
            required: false,
            default: () => ({})
        },
        status: {
            type: String,
            required: true
        }
    },
    methods: {
        async rejectTrade() {
            let data = this.trade
            data['status'] = 'R'
            const req = await this.$axios.put(`contract/${this.trade.id}/`, data)

            if(req.status == 200){
                this.$router.push('/seller/contract')
            }
        },
        async acceptTrade() {
            let data = this.trade
            data['status'] = 'C'
            const req = await this.$axios.put(`contract/${this.trade.id}/`, data)

            if(req.status == 200){
                this.$router.push('/seller/contract')
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

        &-card
            margin: auto

        &-buttons
            display: grid
            grid-template-columns: repeat(2, 1fr)
            gap: .5rem

            &-status-p, &-status-c, &-status-r
                padding: .5rem
                width: fit-content
                height: fit-content
                margin: auto
                grid-column: 1 / -1
                font-weight: bold

                @media screen and (min-width: 1024px)
                    grid-row: 1 / -1
                    margin-left: 0

            &-status
                
                &-p
                    background: #e5d87f
                
                &-c
                    background: #8ae57f

                &-r
                    background: #cf2525

            &-accept, &-reject
                margin: auto
                grid-row: 3
    
            @media screen and (min-width: 1024px)
                grid-template-rows: 1fr 1fr

                &-accept
                    grid-row: 1
                    grid-column: 2

                &-reject
                    grid-row: 2
                    grid-column: 2


        @media screen and (min-width: 480px)
            grid-template-columns: 300px auto

    
            
</style>